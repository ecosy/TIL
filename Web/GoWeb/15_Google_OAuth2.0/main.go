package main

import (
	"context"
	"crypto/rand"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/gorilla/pat"
	"github.com/urfave/negroni"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/google"
)

var googleOauthConfig = oauth2.Config{
	RedirectURL:  "http://localhost:3000/auth/google/callback",
	ClientID:     os.Getenv("GOOGLE_CLIENT_ID"),
	ClientSecret: os.Getenv("GOOGLE_SECRET_KEY"),
	Scopes:       []string{"https://www.googleapis.com/auth/userinfo.email"}, // access 범위- userinfo의 email
	Endpoint:     google.Endpoint,
}

func googleLoginHandler(w http.ResponseWriter, r *http.Request) {

	log.Println("googleLoginHandler started")

	// user가 로그인 후, AuthCodeURL과 Cookie의 state가 같은지 비교함
	state := generateStateOauthCookie(w)        // CSRF attack을 막기 위한 token
	url := googleOauthConfig.AuthCodeURL(state) // user를 보낼 URL 경로

	log.Printf("state : %s\n", state)
	log.Printf("url : %s\n", url)

	// URL로 user를 보냄
	http.Redirect(w, r, url, http.StatusTemporaryRedirect)
}

func generateStateOauthCookie(w http.ResponseWriter) string {

	log.Println("generateStateOauthCookie started")

	expiration := time.Now().Add(1 * 24 * time.Hour) // 1day 이후 만료

	b := make([]byte, 16)
	rand.Read(b) // random 채우기
	state := base64.URLEncoding.EncodeToString(b)
	cookie := &http.Cookie{Name: "OauthState", Value: state, Expires: expiration}
	log.Printf("cookie : %s\n", cookie)
	http.SetCookie(w, cookie)

	return state
}

func googleAuthCallback(w http.ResponseWriter, r *http.Request) {

	log.Println("googleAuthCallback started")

	oauthstate, _ := r.Cookie("OauthState")

	log.Println("Cookie value : ", oauthstate)

	if r.FormValue("state") != oauthstate.Value {
		log.Printf("invalid google oauth state, cookie : %s, state : %s\n", oauthstate.Value, r.FormValue("state"))
		http.Redirect(w, r, "/", http.StatusTemporaryRedirect) // 해커에게 단서를 안주기 위해 기본 경로로 보내줌
	}

	data, err := getGoogleUserInfo(r.FormValue("code"))
	if err != nil {
		log.Println(err.Error())
		http.Redirect(w, r, "/", http.StatusTemporaryRedirect)
	}
	fmt.Fprint(w, string(data))
}

const oauthGoogleUrlAPI = "https://www.googleapis.com/oauth2/v2/userinfo?access_token="

func getGoogleUserInfo(code string) ([]byte, error) {

	log.Println("getGoogleUserInfo started")

	// code와 token 교환
	token, err := googleOauthConfig.Exchange(context.Background(), code)
	if err != nil {
		return nil, fmt.Errorf("Failed to Exchange %s", err.Error())
	}

	log.Println("Token : ", token)

	// token으로 user info 가져오기
	resp, err := http.Get(oauthGoogleUrlAPI + token.AccessToken)
	if err != nil {
		return nil, fmt.Errorf("Failed to get UserInfo %s \n", err.Error())
	}
	log.Println("resp : ", resp)

	return ioutil.ReadAll(resp.Body)
}

func main() {
	mux := pat.New()
	mux.HandleFunc("/auth/google/login", googleLoginHandler)
	mux.HandleFunc("/auth/google/callback", googleAuthCallback)
	n := negroni.Classic()
	n.UseHandler(mux)
	http.ListenAndServe(":3000", n)
}

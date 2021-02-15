# Google Oauth2.0 구현

## 1. 실행방법
1. Google Oauth 등록
* 아래의 강의를 참고하여 Google Oauth 에 등록한다.   

2. git clone 및 실행
```Go
go run main.go
```

## 2. Description
* Go Lang을 사용하여 Google Social Login 기능을 구현함
* [login URL -> Google Auth -> callback URL] 과정을 실행하며 Cookie, Access Token 등 전달되는 정보를 log로 확인할 수 있음

### Refernce
1. https://www.youtube.com/watch?v=BOS73W7s7nU&list=PLy-g2fnSzUTDALoERcKDniql16SAaQYHF&index=16&ab_channel=TuckerProgramming
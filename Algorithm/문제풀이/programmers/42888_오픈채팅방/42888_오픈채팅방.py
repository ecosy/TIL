#%%
# https://programmers.co.kr/learn/courses/30/lessons/42888
#%%
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
#%%
InOut_message = []
user_info = dict()
#%%
import re

for _record in record:
    splited_record = _record.split(" ")

    InOut, uid = splited_record[0], splited_record[1]

    # 입장하는 경우
    if InOut[0] == "E":
        nick_name = splited_record[2]

        # msg 리스트에 추가
        InOut_message.append(f"{nick_name}님이 들어왔습니다.")

        # uid가 존재하지 않는 경우 (첫 입장)
        if uid not in user_info:
            user_info[uid] = {
                "nick_name" : nick_name,
                "InOut_msg_index" : [len(InOut_message)-1]
            }

        # 이미 uid가 존재하는 경우
        else:
            # 기존에 존재하던 msg 닉네임과 다른 경우, 변경 및 업데이트
            if nick_name != user_info[uid]["nick_name"]:
                # 메세지 로그 업데이트
                for index in user_info[uid]["InOut_msg_index"]:
                    InOut_message[index] = re.sub(user_info[uid]["nick_name"], nick_name, InOut_message[index])
                # user info dict 업데이트
                user_info[uid]["nick_name"] = nick_name

            # 새로운 msg 인덱스 추가
            user_info[uid]["InOut_msg_index"].append(len(InOut_message)-1)

    # 닉네임 바꾸는 경우
    elif InOut[0] == "C":
        nick_name = splited_record[2]
        # msg 로그 리스트 업데이트
        for index in user_info[uid]["InOut_msg_index"]:
            InOut_message[index] = re.sub(user_info[uid]["nick_name"], nick_name, InOut_message[index])

        # user info dict 업데이트
        user_info[uid]["nick_name"] = nick_name

    # 퇴장하는 경우
    else:
        # msg 리스트에 추가
        InOut_message.append(f"{user_info[uid]['nick_name']}님이 나갔습니다.")
        user_info[uid]["InOut_msg_index"].append(len(InOut_message)-1)
# %%
InOut_message
# %%
user_info

#%%
####################################
########## solution ################
####################################
#%%
import re
def solution(record):
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    InOut_message = []
    user_info = dict()

    for _record in record:
        splited_record = _record.split(" ")

        InOut, uid = splited_record[0], splited_record[1]

        # 입장하는 경우
        if InOut[0] == "E":
            nick_name = splited_record[2]

            # msg 리스트에 추가
            InOut_message.append(f"{nick_name}님이 들어왔습니다.")

            # uid가 존재하지 않는 경우 (첫 입장)
            if uid not in user_info:
                user_info[uid] = {
                    "nick_name" : nick_name,
                    "InOut_msg_index" : [len(InOut_message)-1]
                }

            # 이미 uid가 존재하는 경우
            else:
                # 기존에 존재하던 msg 닉네임과 다른 경우, 변경 및 업데이트
                if nick_name != user_info[uid]["nick_name"]:
                    # 메세지 로그 업데이트
                    for index in user_info[uid]["InOut_msg_index"]:
                        # InOut_message[index] = re.sub(user_info[uid]["nick_name"], nick_name, InOut_message[index])
                        InOut_message[index] = re.sub(user_info[uid]["nick_name"], nick_name, InOut_message[index])
                    # user info dict 업데이트
                    user_info[uid]["nick_name"] = nick_name

                # 새로운 msg 인덱스 추가
                user_info[uid]["InOut_msg_index"].append(len(InOut_message)-1)

        # 닉네임 바꾸는 경우
        elif InOut[0] == "C":
            nick_name = splited_record[2]
            # msg 로그 리스트 업데이트
            for index in user_info[uid]["InOut_msg_index"]:
                InOut_message[index] = re.sub(user_info[uid]["nick_name"], nick_name, InOut_message[index])
            # user info dict 업데이트
            user_info[uid]["nick_name"] = nick_name

        # 퇴장하는 경우
        else:
            # msg 리스트에 추가
            InOut_message.append(f"{user_info[uid]['nick_name']}님이 나갔습니다.")
            user_info[uid]["InOut_msg_index"].append(len(InOut_message)-1)

    return InOut_message
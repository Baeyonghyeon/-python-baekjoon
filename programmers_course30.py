def solution(participant, completion):
    hash_participant = {}                              # 빈 해쉬 생성
    input_participant(hash_participant, participant)   # 해쉬에 참여선수들을 담음
    hash_completion(hash_participant, completion)      # 해쉬에 담은 참여선수와 비교해서 카운트 제거
    answer = remainder(hash_participant)               #남은 사람 출력
    print("정답은~~ ",answer)
    return answer

#참여선수 담기
def input_participant(hash_participant, participant):
    for loop in participant:
        value = hash_participant.get(loop)
        if value == None:
            hash_participant[loop] = 1;
        else:
            hash_participant[loop] = hash_participant.get(loop) + 1

#참여선수에서 완료선수 빼기
def hash_completion(hash_participant, completion):
    for loop in completion:
        hash_participant[loop] = hash_participant.get(loop) - 1

def remainder(hash_participant):
    for loop in hash_participant:
        if hash_participant[loop] == 1:
            return loop

if __name__ == '__main__':
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    solution(participant, completion)

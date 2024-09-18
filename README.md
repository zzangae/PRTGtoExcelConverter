## PRTG devices, columns URL 가져오기
##### <예제 URL>
`https://PRTGSERVER/api/table.csv?content=devices&columns=objid,name,host,group,probe,parentid&count=*&username=PRTGUSER&passhash=PASSHASH`

##### <추가 컬럼>
`favorite,condition,upsens,downsens,downacksens,partialdownsens,warnsens,pausedsens,unusualsens,undefinedsens,totalsens,schedule,basetype,baselink,notifiesx,intervalx,access,dependency,position,status,comments,priority,message,tags,type,active`

## PRTG devices, columns 를 엑셀파일로 가져오기
##### 1. JSON 설정 파일 만들기
우선, PRTG 서버 정보, ID, 비밀번호를 JSON 파일로 저장합니다. 예를 들어 config.json 파일을 다음과 같이 작성합니다.
<pre>
{
    "prtg_server": "https://PRTG_SERVER",
    "username": "USERNAME",
    "password": "PASSWORD"
}
</pre>
- prtg_server: PRTG 서버 주소 (예: https://192.168.0.1)
- username: PRTG 사용자 ID
- password: PRTG 사용자 비밀번호
##### 2. 라이브러리 설치
- 이 코드를 실행하기 위해서는 pandas와 openpyxl 패키지가 필요합니다. 설치되지 않았다면 다음 명령어로 설치할 수 있습니다 (PowerShell)
<pre>pip install pandas openpyxl</pre>
##### 3. 파이썬 실행
<pre>python JsonToExcel.py</pre>

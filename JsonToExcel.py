import requests
import pandas as pd
import json
import io

# 외부 설정 파일에서 PRTG 서버 정보 및 ID, 비밀번호 읽기
def read_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

# PRTG 데이터를 엑셀 파일로 저장하는 함수
def download_prtg_device_data():
    # 설정 파일에서 서버 정보 읽기
    config = read_config('config.json')
    
    prtg_url = f"{config['prtg_server']}/api/table.csv"
    params = {
        'content': 'devices',                     # 장치 정보를 가져옴
        'columns': 'objid,name,host,group,probe,parentid',  # 필요한 컬럼만 가져옴
        'username': config['username'],
        'password': config['password'],
        'output': 'csvtable'                      # CSV 형식으로 출력
    }

    try:
        # PRTG API 호출 (SSL 인증서 검증 비활성화)
        response = requests.get(prtg_url, params=params, verify=False)
        response.raise_for_status()  # HTTP 에러 체크

        # CSV 데이터를 판다스 데이터프레임으로 읽기
        csv_data = io.StringIO(response.text)
        df = pd.read_csv(csv_data)

        # DataFrame을 엑셀 파일로 저장
        df.to_excel('prtg_devices.xlsx', index=False)

        print("PRTG Device 데이터가 'prtg_devices.xlsx' 파일로 저장되었습니다.")
    
    except requests.exceptions.RequestException as e:
        print(f"PRTG API 호출 중 오류 발생: {e}")

# 함수 호출
download_prtg_device_data()
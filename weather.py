# crawing 네이버에서 날씨를 크롤링. 이미지는 크롤링 불가.
# 텍스트만 크롤링 가능.
# 온도, 어제와 비교온도, 날씨상태, 미세먼지 농도
# 지역을 입력하면 그 지역의 날씨가 출력이 되는 크롤링 윈도우 어플리케이션 만들기.
# 요청 웹브라우저 데이터를 파이썬으로 받아오기 파싱하여 크롤링.
# https://search.naver.com/search.naver?&query=한남동날씨
import requests #pip install requests

from bs4 import BeautifulSoup #pip install beautifulsoup4
userInput = True
while userInput:
   inputArea = input("\n알고 싶은 날씨의 지역을 입력해주세요 :")
   if inputArea == "끝내기":
      print("날씨 정보를 종료합니다.")
      break

   weatherHtml = requests.get(f"https://search.naver.com/search.naver?&query={inputArea}날씨")
   # 네이버에서 한남동날씨로 검색한 결과 html 파일 가져오기
   # print(weatherHtml.text) #.text 써주기

   weatherSoup = BeautifulSoup(weatherHtml.text, 'html.parser')
   # print(weatherSoup)

   # 지역
   # find는 한방에 찾을 때 사용.
   areaText = weatherSoup.find("h2", {"class":"title"}).text #.text 글자만 추출. 날씨 지역 이름 가져오기
   areaText = areaText.strip() # 양쪽 공백제거
   print(f"지역이름 :{areaText}")

   # 현재 온도
   todayTempText = weatherSoup.find("div", {"class":"temperature_text"}).text
   todayTempText = todayTempText[6:12].strip() # 6번째 글자부터 슬라이싱 후 양쪽 공백 제거
   print(f"현재온도 :{todayTempText}") # 슬라이싱 18.5º,

   # 어제와의 날씨 비교
   yesterdayTempText = weatherSoup.find("span",{"class":"temperature"}).text
   yesterdayTempText = yesterdayTempText.strip()

   if yesterdayTempText and yesterdayTempText.find("높아요"):
      print(f"어제보다: {yesterdayTempText}")
   elif yesterdayTempText and yesterdayTempText.find("낮아요"):
      print(f"어제보다: {yesterdayTempText}")

   # 날씨의 상태 맑음
   todayWeatherText = weatherSoup.find("span",{"class":"weather before_slash"}).text
   todayWeatherText.strip()
   print(f"오늘날씨 : {todayWeatherText}")

   # 체감온도
   senseTempText = weatherSoup.find("dd",{"class":"desc"}).text
   senseTempText.strip()    # 맑음
   print(f"체감온도 :{senseTempText}")

   # 미세먼지 농도
   todayInfoText = weatherSoup.select("ul.today_chart_list > li")# 미세먼지, 초미세먼지, 자외선, 일몰
   dust1Info = todayInfoText[0].find("span", {"class":"txt"}).text
   dust1Info = dust1Info.strip()
   print(f"미세먼지 :{dust1Info}")

   # 초미세먼지 농도
   todayInfoText = weatherSoup.select("ul.today_chart_list > li")# 미세먼지, 초미세먼지, 자외선, 일몰
   dust2Info = todayInfoText[1].find("span", {"class":"txt"}).text
   dust2Info = dust2Info.strip()
   print(f"초미세먼지 :{dust2Info}")


str="가나다라마바사"
print(str)
print(str[2])
str2=["네이버","카카오","라인"]
print(str2[1])
print(str2[2][1])
str3="'asdf','zxcv'"
birthday="20240219"
print("현재년도 "+ birthday[0:4]+"년 입니다.")
print("글자수",len(birthday))
cnt=len(birthday)
print("현재월 "+birthday[4:cnt-2],"월 입니다.")
print("현재일 "+birthday[6:],"일 입니다.")
print("년도"+birthday[-6:-4],"년도~")

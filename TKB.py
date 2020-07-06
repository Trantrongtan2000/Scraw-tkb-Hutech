from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()


def an(): #An nut ok cua thong bao
 obj = driver.switch_to.alert
 obj.accept()

driver.get("http://daotao.hutech.edu.vn/default.aspx?page=dangnhap")   #Nhap web va dang nhap
first = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_txtTaiKhoa")
last = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_txtMatKhau")
search = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_btnDangNhap")

first.send_keys("Nhập tài khoản")
last.send_keys("Nhập mật khẩu")
time.sleep(5)

search.click()
time.sleep(5)
an()

driver.get("http://daotao.hutech.edu.vn/default.aspx?page=thoikhoabieu&sta=0")
time.sleep(5)
an()

el = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ctl00_ddlChonNHHK')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Học kỳ 3 - Năm học 2019-2020':
        option.click() # select() in earlier versions of webdriver
        break
time.sleep(5)
an()
tuan=[]
tkb=[]
mon=[]
d={}
tam=[]

t=driver.find_element_by_id('ctl00_ContentPlaceHolder1_ctl00_ddlTuan')
for i in t.find_elements_by_tag_name('option'):
    tuan.append(i.text)

for t1 in range(0,11):
    driver.get("http://daotao.hutech.edu.vn/default.aspx?page=thoikhoabieu&sta=0")
    time.sleep(5)
    an()

    t=driver.find_element_by_id('ctl00_ContentPlaceHolder1_ctl00_ddlTuan')
    for option in t.find_elements_by_tag_name('option'):
        if option.text == tuan[t1]:
            tam.append("\n"+option.text)
            option.click()
            break
    time.sleep(5)
    an()
    for i in range(2,8,1):
        sang=("/html/body/form/div[2]/div/table/tbody/tr[2]/td/div[3]/div[4]/table[1]/tbody/tr[2]/td[%s]"%i)
        chieu=("/html/body/form/div[2]/div/table/tbody/tr[2]/td/div[3]/div[4]/table[1]/tbody/tr[7]/td[%s]"%i)
        m1=driver.find_element(By.XPATH,sang); 
        m2=driver.find_element(By.XPATH,chieu);
        if len(m1.text)!=0 or len(m2.text)!=0:
            chep=[]
            chep.append("\n Thứ "+str(i))
            if len(m1.text)!=0:
                m1=(m1.text).replace("\n",",")
                chep.append('\n Sáng :'+m1)
            if len(m2.text)!=0:
                m2=m2.text.replace("\n",",")
                chep.append("\n Chiều :"+m2)
            con="".join(chep)
            tam.append(con)

    co="".join(tam)
    tkb.append(co)
        

fine="Học kỳ 3 - Năm học 2019-2020\n"+tkb[len(tkb)-1]
tit="TKB Học kỳ 3-Năm học 2019-2020.txt"

file = open("C:/Users/Admin/Desktop/crew bao python/news-crawler/tkb/"+tit, "wb")  #Nhap lien ket toi thu muc can luu
file.write(fine.encode())
file.close()
print("Done!!")

input("\n [Ấn nút bất kì để thoát]")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time
# Khởi tạo trình duyệt (ở đây mình sử dụng Chrome)
driver = webdriver.Chrome()
driver.get("https://thongtintuyengiao.gialai.org.vn/Cuoc-thi-BTG/Cuoc-thi-truc-tuyen/Bai-thi")
def cau1():
# Mở trang web cần kiểm soát


    # Chờ đến khi phần tử trở nên hiển thị trong DOM và sau đó click vào nó
    element = WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="field_cauhoi4"]' ))
    )
    element.click()

    second_element = WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH4_list_0"]'))
    )
    second_element.click()


def cau2():


    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi9"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(2)
    second_element1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH9_list_1"]'))
    )
    second_element1.click()

def cau3():


    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi10"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(2)
    second_element2 = WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH10_list_1"]'))
    )
    second_element2.click()


def cau4():

    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi2"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(2)
    second_element3 = WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH2_list_0"]'))
    )
    second_element3.click()


def cau5():

    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi13"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(2)
    second_element4 = WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH13_list_3"]'))
    )
    second_element4.click()

def cau6():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi8"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element5 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH8_list_3"]'))
    )
    second_element5.click()

def cau7():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi1"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element6 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH1_list_0"]'))
    )
    second_element6.click()

def cau8():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi7"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element7 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH7_list_3"]'))
    )
    second_element7.click()

def cau9():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi15"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element8 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH15_list_0"]'))
    )
    second_element8.click()


def cau10():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi2"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element9 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH2_list_0"]'))
    )
    second_element9.click()


def cau11():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi11"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element10 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH11_list_2"]'))
    )
    second_element10.click()

def cau12():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi10"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(2)
    second_element11 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH10_list_1"]'))
    )
    second_element11.click()

def cau13():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi4"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element12 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH4_list_1"]'))
    )
    second_element12.click()

def cau14():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi12"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element13 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH12_list_0"]'))
    )
    second_element13.click()

def cau15():
    element1 = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field_cauhoi5"]')))
    ActionChains(driver).move_to_element(element1).click().perform()
    time.sleep(1)
    second_element14 = WebDriverWait(driver, 12).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dapanCH5_list_3"]'))
    )
    second_element14.click()

def hovaten():
    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_hovanten_txtText"]')))
    input_element.send_keys("Trần quốc trung")

def ns():
    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_Ngaysinh_txtText"]')))
    input_element.send_keys("02/05/2007")

def diachi():
    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_diachi_txtText"]')))
    input_element.send_keys("Trường THPT Nguyễn Thị Minh Khai")
def dt():
    input_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="p_lt_ctl05_pageplaceholder_p_lt_WebPartZone3_ZoneRight_CustomTableInputEdit_customTableForm_dienthoai_txtText"]')))
    input_element.send_keys("0388189027")

if __name__ == "__main__":
    a = 0.25
    cau1()
    time.sleep(a)
    cau2()
    time.sleep(a)
    cau3()
    time.sleep(a)
    cau4()
    time.sleep(a)
    cau5()
    # time.sleep(a)
    # cau6()
    # time.sleep(a)
    # cau7()
    # time.sleep(a)
    # cau8()
    # time.sleep(a)
    # cau9()
    # time.sleep(a)
    # cau10()
    # time.sleep(a)
    # cau11()
    # time.sleep(a)
    # cau12()
    # time.sleep(a)
    # cau13()
    # time.sleep(a)
    # cau14()
    # time.sleep(a)
    # cau15()
    # time.sleep(a)
    # hovaten()
    # time.sleep(a)
    # ns()
    # time.sleep(a)
    # diachi()
    # time.sleep(a)
    # dt()







time.sleep(10000)



# Đóng trình duyệt
driver.close()

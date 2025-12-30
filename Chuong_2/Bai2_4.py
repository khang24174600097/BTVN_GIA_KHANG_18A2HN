from xml.dom import minidom
tai_lieu = minidom.parse("09_TranDucCo_072_DHKL18A2\BTVN\Chuong_2\sample.xml")
goc = tai_lieu.documentElement
print("Kết quả gốc là: ",goc.tagName)
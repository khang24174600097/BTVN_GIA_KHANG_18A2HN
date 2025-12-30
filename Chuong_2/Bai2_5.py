from xml.dom import minidom

# Đọc file XML
tai_lieu = minidom.parse("09_TranDucCo_072_DHKL18A2\BTVN\Chuong_2\sample.xml")

# Lấy danh sách các phần tử <staff>
danh_sach_nv = tai_lieu.getElementsByTagName("staff")

# In thông tin từng nhân viên
for nv in danh_sach_nv:
    ten = nv.getElementsByTagName("name")[0].firstChild.data
    luong = nv.getElementsByTagName("salary")[0].firstChild.data
    ma_nv = nv.getAttribute("id")
    print(f"Nhân viên {ma_nv}: {ten}, Lương: {luong}")

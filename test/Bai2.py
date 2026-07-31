def tinh_tien_thua(gia, tra):
    thua = gia - tra
    return thua
menh_gia =[ 20, 10,5,2,1]
for x in menh_gia:
    tien_thua = tinh_tien_thua(tra,gia)
    so_tien = tien_thua // x
    tien_thua = tien_thua % x
    print("Số tờ mệnh giá",x,"là:",so_tien)
    
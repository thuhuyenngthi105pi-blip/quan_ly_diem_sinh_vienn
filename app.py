import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")

# 1. Tao du lieu
data = {
    "Họ và tên": [
        "Nguyễn Văn Thuận", 
        "Nguyễn Văn Địch", 
        "Nguyễn Thị Hiền", 
        "Nguyễn Thị Lan",
        "Trần Thị Hạnh",
        "Nguyễn Văn Thắng",
        "Nguyễn Anh Tuấn",
        "Nguyễn Minh Nhật",
        "Nguyễn Minh Khôi",
        "Nguyễn Duy Khánh"
    ],
    "Chuyên cần": [9, 8, 10, 7, 8, 9, 6, 10, 7, 9],
    "Giữa kỳ": [8, 7, 9, 6, 7, 8, 5, 9, 6, 8],
    "Cuối kỳ": [9, 8, 9, 7, 8, 9, 6, 10, 7, 9]
}

df = pd.DataFrame(data)

# 2. Tinh diem tong ket
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
)

# 3. Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 4. Tieu de va bang diem
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(
    df.style.format({"Tổng kết": "{:.2f}"}),
    use_container_width=True,
    hide_index=True
)

# 5. Thong ke
st.subheader("Thống kê kết quả")

cot1, cot2, cot3, cot4 = st.columns(4)

cot1.metric("Điểm trung bình lớp", f"{df['Tổng kết'].mean():.2f}")
cot2.metric("Điểm cao nhất", f"{df['Tổng kết'].max():.2f}")
cot3.metric("Điểm thấp nhất", f"{df['Tổng kết'].min():.2f}")
cot4.metric("Số sinh viên đạt", f"{(df['Tổng kết'] >= 5).sum()}/10")

st.write("**Sinh viên điểm cao nhất:**")
st.write(df.loc[df["Tổng kết"] == df["Tổng kết"].max(), "Họ và tên"].tolist())

st.write("**Sinh viên điểm thấp nhất:**")
st.write(df.loc[df["Tổng kết"] == df["Tổng kết"].min(), "Họ và tên"].tolist())

# 6. Chon sinh vien
st.subheader("Tra cứu điểm sinh viên")

ten = st.selectbox("Chọn sinh viên:", df["Họ và tên"])
sv = df[df["Họ và tên"] == ten].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", f"{sv['Chuyên cần']:.1f}")
c2.metric("Giữa kỳ", f"{sv['Giữa kỳ']:.1f}")
c3.metric("Cuối kỳ", f"{sv['Cuối kỳ']:.1f}")
c4.metric("Tổng kết", f"{sv['Tổng kết']:.2f}")
c5.metric("Xếp loại", sv["Xếp loại"])

# 7. Bieu do
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Họ và tên"], df["Tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 8. Thong tin nguoi tao
st.divider()
st.caption("Người tạo: NGUYỄN THỊ THU HUYỀN | MSSV: 026308006010")

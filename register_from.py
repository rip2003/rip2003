import flet as ft
import csv
import os

CSV_FILE = "สมัครสมาชิก.csv"

def main(page: ft.Page):
    page.title = "ฟอร์มสมัครสมาชิก"
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    # สร้างช่องกรอกข้อมูล
    name = ft.TextField(label="ชื่อ-สกุล", width=300)
    phone = ft.TextField(label="หมายเลขโทรศัพท์", width=300, keyboard_type=ft.KeyboardType.PHONE)
    team = ft.TextField(label="ชื่อทีม", width=300)
    status = ft.Text("")

    def save_data(e):
        if not name.value or not phone.value or not team.value:
            status.value = "กรุณากรอกข้อมูลให้ครบทุกช่อง"
            status.color = "red"
        else:
            file_exists = os.path.isfile(CSV_FILE)

            with open(CSV_FILE, mode="a", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["ชื่อ-สกุล", "เบอร์โทร", "ชื่อทีม"])  # เขียนหัวตารางถ้ายังไม่มี
                writer.writerow([name.value, phone.value, team.value])

            status.value = "✅ บันทึกข้อมูลเรียบร้อย"
            status.color = "green"

            # ล้างข้อมูลในฟอร์ม
            name.value = ""
            phone.value = ""
            team.value = ""

        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("📋 ฟอร์มสมัครสมาชิก", size=20, weight="bold"),
                name,
                phone,
                team,
                ft.ElevatedButton(text="บันทึกข้อมูล", on_click=save_data),
                status
            ],
            alignment="start",
            spacing=20,
        )
    )

ft.app(target=main)

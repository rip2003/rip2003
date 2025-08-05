import flet as ft

def main(page: ft.Page):
    page.title = "เครื่องคิดเลข (Calculator)"
    page.window_width = 300
    page.window_height = 400
    page.window_resizable = False

    expression = ft.TextField(value="", read_only=True, text_align="right", expand=True)

    def button_click(e):
        value = e.control.text
        if value == "=":
            try:
                expression.value = str(eval(expression.value))
            except Exception:
                expression.value = "Error"
        elif value == "C":
            expression.value = ""
        else:
            expression.value += value
        page.update()

    # ปุ่มที่จะแสดง
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"]
    ]

    # สร้าง Layout ของปุ่ม
    rows = []
    for row in buttons:
        button_row = []
        for btn in row:
            button_row.append(
                ft.ElevatedButton(
                    text=btn,
                    width=60,
                    height=60,
                    on_click=button_click
                )
            )
        rows.append(ft.Row(controls=button_row, alignment="center"))

    # แสดงทั้งหมดในหน้า
    page.add(
        expression,
        *rows
    )

# เรียกใช้งาน Flet app
ft.app(target=main)

import sys
from collections import defaultdict

tasks = []

def show_menu():
    print("\n=== เมนูจัดการงานฟาร์ม ===")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    name = input("ชื่องาน: ")
    category = input("ประเภท (พืช/สัตว์): ")
    tasks.append({"name": name, "category": category})

    print(f"✅ เพิ่มงาน '{name}' แล้ว")

def show_tasks():
    if not tasks:
        print("🚫 ยังไม่มีงานในระบบ")
    else:
        print("\n📋 รายการงานทั้งหมด:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} ({task['category']})")

def delete_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("เลือกหมายเลขงานที่ต้องการลบ: ")) - 1
            removed = tasks.pop(index)
            print(f"🗑 ลบงาน '{removed['name']}' แล้ว")
        except (IndexError, ValueError):
            print("❌ เลือกไม่ถูกต้อง")

def summarize_tasks():
    summary = defaultdict(int)
    for task in tasks:
        summary[task['category']] += 1

    print("\n📊 สรุปงานตามประเภท:")
    for category, count in summary.items():
        print(f"- {category}: {count} งาน")

def main():
    while True:
        show_menu()
        choice = input("เลือกเมนู (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            summarize_tasks()
        elif choice == '5':
            print("👋 ออกจากโปรแกรมแล้ว")
            sys.exit()
        else:
            print("❗ กรุณาเลือกเมนู 1-5")

if __name__ == "__main__":
    main()
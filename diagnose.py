import obd

# Establish connection with the OBD-II adapter
# إنشاء اتصال مع محول OBD-II
connection = obd.OBD()

if connection.is_connected():
    print("✅ Connection established! Running vehicle diagnostics...")
    print("✅ تم الاتصال! جاري تشغيل تشخيص السيارة...\n")

    def check_value(command, min_value, max_value, name, unit=""):
        response = connection.query(command)
        if response.value is not None:
            value = response.value.magnitude
            status = "✅ OK" if min_value <= value <= max_value else "❌ Error"
            arabic_status = "✅ سليم" if min_value <= value <= max_value else "❌ خطأ"
            print(f"{name}: {value} {unit} → {status} / {arabic_status}")
            return status
        else:
            print(f"{name}: ❌ No value available / ❌ لا توجد قيمة متاحة")
            return "Error"

    # Checking key vehicle components
    # فحص المكونات الرئيسية للسيارة
    check_value(obd.commands.RPM, 600, 7000, "Engine RPM / عدد دورات المحرك", "rpm")
    check_value(obd.commands.SPEED, 0, 300, "Speed / السرعة", "km/h")
    check_value(obd.commands.COOLANT_TEMP, 70, 110, "Coolant Temperature / درجة حرارة سائل التبريد", "°C")
    check_value(obd.commands.THROTTLE_POS, 0, 100, "Throttle Position / وضع دواسة الوقود", "%")
    check_value(obd.commands.MAF, 2, 50, "Mass Air Flow Sensor / مستشعر تدفق الهواء", "g/s")
    check_value(obd.commands.INTAKE_PRESSURE, 10, 100, "Intake Pressure / ضغط السحب", "kPa")
    check_value(obd.commands.O2_S1_WR_CURRENT, -1, 1, "Oxygen Sensor / مستشعر الأكسجين", "mA")

    # Read error codes
    # قراءة رموز الأخطاء
    dtc_response = connection.query(obd.commands.GET_DTC)
    if dtc_response.value:
        print("\n🚨 Error codes detected:")
        print("\n🚨 تم اكتشاف رموز أخطاء:")
        for code in dtc_response.value:
            print(f" - {code}")
    else:
        print("\n✅ No error codes detected!")
        print("\n✅ لم يتم اكتشاف أي رموز أخطاء!")

else:
    print("❌ Failed to connect to the OBD-II adapter!")
    print("❌ فشل الاتصال بمحول OBD-II!")

# Close connection
# إغلاق الاتصال
connection.close()

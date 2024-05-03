# Digital Shopkeeper
name = str(input("貴賓您好,請問尊姓大名?\n"))
while True:
    option = float(input(f"您好{name},歡迎蒞臨 郝便宜百貨,\n請問今天需要什麼服務呢?\n"
                         f" (1)購買服飾 (2)健康諮詢 (3)美食饗宴 (4)複利計算機 (5)離開服務 (*ps請輸入數字1,2,3,4)\n"))

# [Function 1 購買服飾] -- for-loop 迴圈 2多重條件if判定 list集合 
# (1)挑選商品種類 (2)公布售價和款式讓顧客選擇商品 (3)詢問尺寸
# (4)檢定次數 且 詢問繼續購物與否,若False則打破迴圈 (5)結算付款

# 自定義函式 #輸入身高體種 尺寸選擇判定

    def choose_size():
        height = float(input("請輸入您的身高(公分)\n"))
        weight = float(input("請輸入您的體重(公斤)\n"))

        if height >= 180 or weight >= 100:
            size = "XL"
            print(f"您的尺寸為{size}")
        elif height >= 175 or weight >= 80:
            size = "L"
            print(f"您的尺寸為{size}")
        elif height >= 170 or weight >= 65:
            size = "M"
            print(f"您的尺寸為{size}")
        elif height >= 160 or weight >= 60:
            size = "S"
            print(f"您的尺寸為{size}")
        else:
            size = "XS"
            print(f"您的尺寸為{size}")


    times = 1
    if option == 1:
        cart = []
        list_clothes = {"Mike限量上衣": 800, "阿弟達排汗衫": 500}
        list_pants = {"普馬短褲": 500, "古奇運動褲": 900}
        list_shoes = {"Confident板鞋": 2000, "橋登簽名籃球鞋": 5000}
        total = 0
        while True:
            # 檢定次數
            if times < 2:
                times += 1
                twice = ""
            else:
                twice = "還"
            items = int(input(
                f"請問{name}您{twice}想購買甚麼種類的服飾呢?\n(1)衣服 (2)褲子 (3)鞋子 (4)檢視購物車 (5)結束購物\n"))

            if items == 1:
                print(f"請參考看看喔\n + {list_clothes}\n")
                clothes = str(input("請輸入商品名稱(ps.建議直接複製選項)\n"))
                cart.append(clothes)
                if list_clothes.get(clothes) is None:
                    print("無此項商品請您重新輸入")
                else:
                    # cart.append(clothes)
                    total += list_clothes.get(clothes)
                    choose_size()  # 自定義函式
            elif items == 2:
                print(f"請參考看看喔\n + {list_pants}\n")
                pants = str(input("請輸入商品名稱(ps.建議直接複製選項)\n"))
                cart.append(pants)
                if list_pants.get(pants) is None:
                    print("無此項商品請您重新輸入")
                else:
                    # cart.append(pants)
                    total += list_pants.get(pants)
                choose_size()  # 自定義函式
            elif items == 3:
                feet_size = float(input("請輸入您的足長(cm)\n"))
                print(f"請參考看看喔 + {list_shoes}")
                shoes = str(input("請輸入商品名稱(ps.建議直接複製選項)\n"))
                cart.append(shoes)
                if list_shoes.get(shoes) is None:
                    print("無此項商品請您重新輸入")
                else:
                    # cart.append(shoes)
                    total += list_shoes.get(shoes)

            elif items == 4:
                print(f"您的購物車內有:{cart}")

            elif items == 5:
                print(f"您的總金額為{total}新台幣,")
                break
            else:
                print("請輸入有效數值")

    # [Function 2 健康諮詢] -- 性別係數 多變數運算
    # (1)BMI健康諮詢 (2)BMR計算(基礎代謝率) (3)TDEE計算(總熱量消耗)
    elif option == 2:
        mode = str(input(
            f"歡迎{name}使用健康諮詢服務,請選擇您要使用的功能,輸入數字(1 or 2 or 3)\n(1)BMI計算機\n(2)BMR計算(基礎代謝率)\n(3)TDEE計算(總熱量消耗)\n"))
        # 輸入資料
        height = float(input("請輸入您的身高(公分)\n"))
        weight = float(input("請輸入您的體重(公斤)\n"))
        BMI = round(weight / ((height / 100) ** 2), 1)
        # (1)BMI計算機
        # 公式:體重(公斤)/身高(公尺)**2
        if mode == "1":
            if BMI < 15.5:
                health = "體重超輕,\n建議:前往醫院檢查腸胃健康與否,也有可能腹部有寄生蟲,每餐攝取多一些的碳水,以維持身體正常機能"
            elif BMI < 18.5:
                health = "體重過輕,\n建議:每餐攝取多一些的碳水,以維持身體正常機能"
            elif BMI < 24:
                health = "正常體重,\n健康狀況良好!請繼續維持"
            elif BMI < 27:
                health = "體重過重,易成為為心血管疾病高風險族群\n建議:減少 攝取碳水化合物 以及 每周 1~3 次輕中度有氧運動"
            elif BMI < 30:
                health = "輕度肥胖,為心血管疾病高風險族群\n建議:減少 攝取碳水化合物 以及 每周 1~3 次中度有氧運動"
            elif BMI < 35:
                health = "中度肥胖,易造成心血管疾病\n建議:實施飲食控管,少油少糖少鹽以及每周 2~4 次高強度有氧運動"
            else:
                health = "重度肥胖,極易造成心血管疾病\n建議:實施飲食控管,以及每周 3~5 次高強度有氧運動,"
            print(f"檢驗報告\n--------\n{name}您的BMI是:{BMI} 屬於{health}\n")
        # (2)BMR計算(基礎代謝率)

        elif mode == "2":
            gender = str(input("請輸入您的生理性別(M or F)(男性 or 女性)\n")).upper()
            age = int(input("請輸入您的年齡\n"))

            if gender == "M" or "Male" or "男性":
                BMR = round(66 + (13.7 * weight) + 5 * height - 6.8 * age, 1)
                print(f"檢驗報告\n--------\n{name}您的BMR值為{BMR}\n")
            elif gender == "F" or "Female" or "女姓":
                BMR = round(655 + (9.6 * weight) + 1.8 * height - 4.7 * age, 1)
                print(f"檢驗報告\n--------\n{name}您的BMR值為{BMR}\n")
            else:
                print("請重新輸入有效生理性別")
        # (3)TDEE計算(總熱量消耗)
        elif mode == "3":
            value = 0
            TDEE = 0
            BMR = 0
            how_often = str(input(
                "請問選擇最符合您一周運動量的描述,輸入A-E其一選項\n""(A) 久坐,幾乎沒運動\n""(B) 每周低強度運動1~3天\n""(C) 每周中強度運動3~5天\n"
                "(D) 每周高強度運動6~7天\n""(E) 勞力密集或是每天高強度運動\n")).upper()
            gender = str(input("請輸入您的生理性別(M or F)(男性 or 女性)\n")).upper()

            age = int(input("請輸入您的年齡\n"))
            if gender == "M" or "Male" or "男性":
                BMR += round(66 + (13.7 * weight) + 5 * height - 6.8 * age, 1)
            elif gender == "F" or "Female" or "女姓":
                BMR += round(655 + (9.6 * weight) + 1.8 * height - 4.7 * age, 1)

            if how_often == "A":
                value += 1.2
            elif how_often == "B":
                value += 1.375
            elif how_often == "C":
                value += 1.55
            elif how_often == "D":
                value += 1.725
            elif how_often == "E":
                value += 1.9
            else:
                print("請輸入有效選項")
            TDEE = BMR * value
            print(f"{name}您的TDEE數值為: {round(TDEE,2)}")
        # (4)debug
        else:
            print("請輸入1-3其中一個數字")

    # [Function 3 美食饗宴] -- 選項判斷加價與否 加料推薦 三重判斷結算總金額
    elif option == 3:
        print("歡迎使用拉麵點餐機\n(1)鹽味拉麵 $220\n(2)醬油拉麵 $240\n(3)豚骨拉麵 $280")
        flavor = (input("請選擇拉麵口味(輸入:1,2,3)\n"))

        # 口味選擇
        soup = 0
        if flavor == "1":
            print("好的,一份鹽味拉麵")
            soup += 220
        elif flavor == "2":
            print("好的,一份醬油拉麵")
            soup += 240
        elif flavor == "3":
            print("好的,一份豚骨拉麵")
            soup += 280
        # debug
        else:
            print("先生/女士,新品尚未上市 敬請期待")

        # 是否加大 (豚骨另計)
        size = (input("需要加大嗎,豚骨口味+$50,其他口味+$30 (輸入Y or N)"))
        if flavor == "3" and size == "Y":
            size_price = 50
        elif flavor == "1" or "2" and size == "Y":
            size_price = 30
        else:
            size_price = 0

        # 是否加糖心蛋
        egg = (input("我們家的糖心蛋很好吃呦! 要幫您做加點嗎? 一份是$30 (輸入Y or N)"))
        if egg == "Y":
            egg_price = 30
        else:
            egg_price = 0

        # 是否加叉燒
        pork = (input("叉燒的肉質也很軟嫩,需要幫您做加點嗎? 一份是$60 (輸入Y or N)"))
        if pork == "Y":
            pork_price = 60
        else:
            pork_price = 0

        # 是否折扣
        if size == "Y" and egg == "Y" and pork == "Y":
            discount = 20
            print("加好加滿,幫您折$20")
        else:
            discount = 0

        total = (soup + size_price + egg_price + pork_price - discount)
        print(f"感謝您本次的消費,這樣一共是" + str(total) + "元整,期待您的下次光臨")

    # [Function 4 複利計算機] -- 基礎運算符號
    elif option == 4:
        money = float(input("請您輸入本金金額\n"))
        rate = float(input("請輸入年利率(單位%)\n"))
        month = int(input("請問幾個月複利一次?\n"))
        period = float(input("預計存放幾年?\n"))
        total = float((money * (1 + rate / 100) ** (period * 12 / month)))
        print(f"{name},您的期望存款為{round(total, 2)}元整\n")

    elif option == 5:
        print("謝謝惠顧,期待您再次蒞臨本店")
        break
    # [DeBug ]
    else:
        print("請重新輸入有效數值1-5")

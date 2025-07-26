from typing import Optional


def get_faq_response(text: str) -> Optional[str]:
    text = text.lower()
    if any(
        word in text
        for word in [
            "價格",
            "收費",
            "費用",
            "多少錢",
            "月費",
            "年費",
            "包月",
            "price",
            "fee",
            "cost",
            "charge",
            "membership",
        ]
    ):
        return "中文: 我們免年費免會費，包月或以分計費自由選，用多少扣多少，歡迎洽詢！\nEnglish: No annual or membership fee. Flexible monthly or pay-per-use options. Only pay for what you use! Contact us for details."
    elif any(
        word in text
        for word in ["地址", "怎麼去", "在哪", "地點", "address", "location", "where"]
    ):
        return "中文: 我們的地址是：新北市中和區景平路690號，靠近捷運中和站。\nEnglish: Our address: No. 690, Jingping Rd., Zhonghe District, New Taipei City (near Zhonghe MRT Station)."
    elif any(
        word in text for word in ["電話", "聯絡", "客服", "phone", "call", "contact"]
    ):
        return "中文: 您可以撥打 02 2248 6991 聯絡我們，或加LINE/IG: fitopia2021。\nEnglish: You can call us at 02 2248 6991 or contact us via LINE/IG: fitopia2021."
    elif any(word in text for word in ["email", "信箱"]):
        return "中文: 我們的Email是 kiridofit@gmail.com\nEnglish: Our email: kiridofit@gmail.com"
    elif any(
        word in text
        for word in [
            "營業",
            "開放",
            "時間",
            "幾點",
            "hour",
            "open",
            "close",
            "business",
        ]
    ):
        return "中文: 營業時間是: 每天早上9點到凌晨1點\nEnglish: Business hours: 9:00 AM to 1:00 AM every day."
    elif any(
        word in text
        for word in ["粉絲專頁", "facebook", "ig", "instagram", "社群", "line"]
    ):
        return (
            "中文: FB/IG/LINE: fitopia2021\nEnglish: Follow us: FB/IG/LINE: fitopia2021"
        )
    elif text in ["hi", "hello"]:
        return "中文: Hello! How can I help you today?\nEnglish: Hello! How can I help you today?"
    elif text == "bye":
        return "中文: 掰掰!\nEnglish: Goodbye!"
    elif text in ["thanks", "thank you"]:
        return "中文: 不客氣!\nEnglish: You’re welcome!"
    elif any(
        word in text
        for word in [
            "團練楊姐",
            "楊姐",
        ]
    ):
        return (
            "中文: 團練楊姐是醉\nEnglish: Coach Yang is our group training instructor."
        )
    return None

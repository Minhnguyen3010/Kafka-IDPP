# utils/data_converter.py

def convert_data(org_data: dict) -> dict:
    """
    Chuyển đổi dữ liệu từ topic 'org' sang topic 'std'.

    org_data gồm các trường:
        - TAG_ID
        - Org_Time
        - Col_Time
        - Value

    std_data sẽ gồm:
        - TAG_ID (giữ nguyên)
        - STD_ID (mapping từ TAG_ID)
        - Plant_CD (mã nhà máy cố định hoặc sinh động)
    """

    # Mapping đơn giản: STD_ID = "STD_" + TAG_ID
    tag_id = org_data.get("TAG_ID")
    org_time = org_data.get("Org_Time")
    col_time = org_data.get("Col_Time")
    value = org_data.get("Value")
    std_id = f"STD_{tag_id}"

    # Plant code có thể cố định hoặc lấy từ config
    plant_cd = "PLANT01"

    std_data = {
        "TAG_ID": tag_id,
        "Org_Time": org_time,
        "Col_Time": col_time,
        "Value": value,
        "STD_ID": std_id,
        "Plant_CD": plant_cd
    }

    return std_data

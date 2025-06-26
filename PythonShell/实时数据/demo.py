import akshare as ak
import pandas as pd

# index_zh_a_hist_min_em_df_513580 = ak.index_zh_a_hist_min_em(
#     symbol="513580",
#     period="1",
#     start_date="2025-04-17 09:30:00",
#     end_date="2025-04-17 15:00:00",
# )

stock_hk_index_daily_em_HS2083 = ak.stock_hk_index_spot_em(
    symbol="HSI",
    # period="1",
    # start_date="2025-04-17 09:30:00",
    # end_date="2025-04-17 15:00:00",
)
print(stock_hk_index_daily_em_HS2083)

# 使用 ExcelWriter 写入多个工作表
with pd.ExcelWriter("test.xlsx") as writer:
    #     index_zh_a_hist_min_em_df_513580.to_excel(writer, sheet_name="513580")
    stock_hk_index_daily_em_HS2083.to_excel(writer, sheet_name="HS2083")

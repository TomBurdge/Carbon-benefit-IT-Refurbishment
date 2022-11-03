import pandas as pd

df = pd.read_csv('boavizta-data-us.csv')

#add a save CSV save function into these when confident that they work, or just progress to calculating the mean

def create_category_df(type):
    mask = df['subcategory'] == str(type)
    df_new = df[mask].copy()
    return df_new

def create_category_df_screen_greater(type, number):
    mask = df['subcategory'] == str(type)
    more_than_x_mask = df['screen_size'] > float(number)
    df_new = df[mask&more_than_x_mask].copy()
    return df_new

def create_category_df_screen_lesser(type, number):
    mask = df['subcategory'] == str(type)
    less_than_x_mask = df['screen_size'] < float(number)
    df_new = df[mask&less_than_x_mask].copy()
    return df_new

def subcategory_mask(type):
    return df['subcategory'] == str(type)

desktop_mask = subcategory_mask('Desktop')
empty_screen_mask = df['screen_size'].isnull()
phone_mask = subcategory_mask('Smartphone')
tablet_mask = subcategory_mask('Tablet')
thin_client_mask_1 = subcategory_mask('Thin client')
thin_client_mask_2 = subcategory_mask('Thin Client')


df_all_notebook = create_category_df('Laptop')
df_notebook_more_than_14 = create_category_df_screen_greater('Laptop',14.0)
df_notebook_less_than_14 = create_category_df_screen_lesser('Laptop',14.0)
df_aio_desktop = df[desktop_mask & ~empty_screen_mask].copy()
df_desktop_no_screen = df[desktop_mask & empty_screen_mask].copy()
df_thin_client = create_category_df(thin_client_mask_1|thin_client_mask_2)
#USDT, SFF, Tower - use regex from previous
df_monitor_all = create_category_df('Monitor')
df_monitor_greater_33 = create_category_df_screen_greater('Monitor',33.0)
df_monitor_lesser = create_category_df_screen_lesser('Monitor',33.0)
df_all_printer = create_category_df('Printer')
df_server = create_category_df('Server')
df_handheld = create_category_df(phone_mask|tablet_mask)
df_tablet = create_category_df('Tablet')
df_smartphone = create_category_df('Smartphone')
#no projector
df_network = create_category_df('Network') #Network files on this not so many - will need to see if can find more

#print(df_monitor_all.sample(3))
print(df_notebook_more_than_14.columns.to_list())

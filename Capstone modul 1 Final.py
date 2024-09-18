import pwinput #u/ masking password yang di input
from colorama import Fore, Style, init #Fore : Warna text, Style : gaya text (reset)
from tabulate import tabulate

#Dictionary product_dict, key : nama produk, value : detail produk
product_dict = {
    'Macbook Air': {'ID': 1, 'category': 'Laptop', 'warranty': '2 Year', 'price': 22000000, 'stock': 15},
    'Macbook Pro': {'ID': 2, 'category': 'Laptop', 'warranty': '2 Year', 'price': 32000000, 'stock': 15},
    'iMac': {'ID': 3, 'category': 'Desktop', 'warranty': '2 Years', 'price': 30000000, 'stock': 10},
    'iPad Pro': {'ID': 4, 'category': 'Tablet', 'warranty': '1 Years', 'price': 21000000, 'stock': 20},
    'iPad Air': {'ID': 5, 'category': 'Tablet', 'warranty': '1 Year', 'price': 12000000, 'stock': 20},
    'iPad Mini': {'ID': 6, 'category': 'Tablet', 'warranty': '1 Year', 'price': 10000000, 'stock': 20},
    'iPhone 15 Pro': {'ID': 7, 'category': 'Smartphone', 'warranty': '1 Year', 'price': 25000000, 'stock': 30},
    'iPhone 15': {'ID': 8, 'category': 'Smartphone', 'warranty': '1 Year', 'price': 20000000, 'stock': 30},
    'iPhone 14 Pro': {'ID': 9, 'category': 'Smartphone', 'warranty': '1 Year', 'price': 15000000, 'stock': 25},
    'iPhone 14': {'ID': 10, 'category': 'Smartphone', 'warranty': '1 Year', 'price': 11000000, 'stock': 25},
    'iPhone 13': {'ID': 11, 'category': 'Smartphone', 'warranty': '1 Year', 'price': 10000000, 'stock': 20},
    'iPhone 12': {'ID': 12, 'category': 'Smartphone', 'warranty': '1 Year', 'price': 8000000, 'stock': 15},
    'Apple Watch Ultra': {'ID': 13, 'category': 'Wearable', 'warranty': '6 Months', 'price': 15000000, 'stock': 20},
    'Apple Watch SE': {'ID': 14, 'category': 'Wearable', 'warranty': '6 Months', 'price': 6000000, 'stock': 15},
    'AirPods Pro': {'ID': 15, 'category': 'Accessory', 'warranty': '6 Months', 'price': 4500000, 'stock': 30},   
    'AirPods Max': {'ID': 16, 'category': 'Accessory', 'warranty': '6 Months', 'price': 8000000, 'stock': 30},   
}

# MEMBUAT FUNGSI MENU TAMPILKAN PRODUK
def format_IDR (amount):
    return 'IDR {:,}'.format(int(amount)) #ribuan dipisahkan dengan (,) & tidak ada pecahan (int)

def display_product():
    print(Fore.CYAN + '================================= PRODUCT LIST =================================' + Style.RESET_ALL) #judul tabel
    product_list = [] #list kosong u/ menyimpan data produk
    for product, details in product_dict.items(): #For loop untuk menyusun data produk yang berisi nama produk dan details nya. items u/ memanggil key-value dict
        format_price = format_IDR(details['price'])
        product_list.append([details['ID'], product, details['category'], details['warranty'], format_price, details['stock']])#menambahkan semua informasi produk ke list kosong
    print(tabulate(product_list, headers=['ID', 'PRODUCT', 'CATEGORY', 'WARRANTY', 'PRICE', 'STOCK'], tablefmt='grid')) 

    while True: #Setelah menampilkan tabel fungsi masuk ke while loop u/ tekan enter
        user_input = input(Fore.YELLOW + 'Press "Enter" to continue...' + Style.RESET_ALL)
        if user_input == '':
            break
        else:
            print(Fore.RED + 'Invalid input. Please press "Enter" to continue.' + Style.RESET_ALL)

# MEMBUAT FUNGSI MENU TAMBAH PRODUK
password_admin = '1234'

def admin_login():
    password = pwinput.pwinput(Fore.BLUE + 'Enter the admin password: ' + Style.RESET_ALL, mask='*') #function u/ masking
    if password == password_admin:
        print(Fore.GREEN + 'Access granted' + Style.RESET_ALL)
        return True #mengembalikan True jika kondisi terpenuhi
    else:
        print(Fore.RED + 'Access Denied. Returning to main menu.' + Style.RESET_ALL)
        main()  

def format_product_name(name):
    return name.lower().replace(' ', '') #untuk membuat nama produk tanpa spasi dan huruf kapital

def add_product():
    formatted_product_dict = {format_product_name(name): name for name in product_dict.keys()} #dictionary baru u/ memeriksa duplicate produk
    
    while True: #while loop utama untuk input nama produk hingga valid serta memerika duplikasi
        product = input(Fore.BLUE + 'Enter product name to add : ' + Style.RESET_ALL)
        formatted_product = format_product_name(product) #menyimpan nama produk yang sudah diformat
        
        if formatted_product in formatted_product_dict :
            existing_product = formatted_product_dict[formatted_product] #memerika apakah formatted_product ada di dict baru
            print(Fore.RED + f'{existing_product} already exists in inventory. Please enter a different name.' + Style.RESET_ALL)
        else:
            category = input(Fore.BLUE + f'Enter category of {product}: ' + Style.RESET_ALL)
            warranty = input(Fore.BLUE + f'Enter warranty of {product}: ' + Style.RESET_ALL)
            
            while True: #while loop untuk cek validasi input harga
                try:
                    price = int(input(Fore.BLUE + f'Enter price of {product}: ' + Style.RESET_ALL))
                    break
                except ValueError: #untuk menangani input yang tidak valid (bukan angka)
                    print(Fore.RED + 'Invalid input. Please enter a valid number for price.' + Style.RESET_ALL)
            
            while True: #while loop untuk cek validasi input stock
                try:
                    stock = int(input(Fore.BLUE + f'Enter stock of {product}: ' + Style.RESET_ALL))
                    break
                except ValueError:
                    print(Fore.RED + 'Invalid input. Please enter a valid number for stock.' + Style.RESET_ALL)

            new_id = max(details['ID'] for details in product_dict.values()) + 1 #menentukan id baru, mengambil id maksimum ditambah 1
            
            print(Fore.MAGENTA + '\nCheck the details below before adding the product :' + Style.RESET_ALL) #menampilan rincian produk yg akan ditambahakan
            print(f'Name: {product}')
            print(f'Category: {category}')
            print(f'Warranty: {warranty}')
            print(f'Price: {price}')
            print(f'Stock: {stock}')
            
            while True: #while loop u/ konfirmasi user sebelum menambahkan produk
                confirm = input(Fore.CYAN + 'Do you want to add this product to Product List? (y / n) : ' + Style.RESET_ALL).lower()
                
                if confirm not in ['y', 'n'] : #memeriksa apakah input pengguna 'y' atau 'n' 
                    print(Fore.RED + 'Invalid input! Please enter "y" for yes or "n" for no.' + Style.RESET_ALL)
                    continue #kembali k loop awal
                
                if confirm == 'y': #jika 'y' produk akan ditambahkan ke dictionary
                    product_dict[product] = {'ID': new_id, 'price': price, 'stock': stock, 'category': category, 'warranty': warranty}
                    print(Fore.GREEN + f'{product} added to Product List.' + Style.RESET_ALL)
                    display_product()
                else:
                    print(Fore.RED + 'Product addition cancelled. Returning to the main menu.' + Style.RESET_ALL) #jika input 'n' kembali ke menu utama
                break #keluar dari loop baik 'y' atau 'n'
            main()

# MEMBUAT FUNGSI MENU HAPUS PRODUK
def remove_product():
    display_product()
    
    while True:
        try: 
            product_id = int(input(Fore.BLUE + 'Enter the ID of the product to remove : ' + Style.RESET_ALL))
            
            product_to_remove = None #membuat variabel u/ menyimpan nama produk (sesuai ID) yg akan dihapus
            for product, details in product_dict.items():
                if details['ID'] == product_id: #cek id di dict cocok dengan id input
                    product_to_remove = product #jika cocok disimpan disini
                    break #menghentikan loop setelah produk cocok ditemukan
            
            if product_to_remove:
                while True: #while loop u/ konfirmasi penghapusan produk
                    confirmation = input(Fore.CYAN + f'Do you want to remove ID {product_id} : {product} from Product List? (y / n) : ' + Style.RESET_ALL).lower()

                    if confirmation == 'y':
                        del product_dict[product_to_remove] #menghapus produk dari produk dict
                        print(Fore.GREEN + f'Product with ID {product_id} has been removed.' + Style.RESET_ALL)
                        break  

                    elif confirmation == 'n':
                        print(Fore.RED + 'Product removal canceled. Returning to main menu.' + Style.RESET_ALL)
                        break  
                    else: #ketika input bukan 'y' atau 'n'
                        print(Fore.RED + 'Invalid input! Please enter "y" for yes or "n" for no.' + Style.RESET_ALL)
                break  
                
            else: #jika produk id diluar yang ada di list produk
                print(Fore.RED + f'No product found with ID {product_id}. Please try again.' + Style.RESET_ALL)
        
        except ValueError: #jika input bukan integer
            print(Fore.RED + 'Invalid input! Please enter a valid number of the product ID.' + Style.RESET_ALL)
    
    display_product()

# MEMBUAT FUNGSI MENU UBAH PRODUK
def update_product():
    while True:
        display_product()
        
        while True: #memeriksa apakah id yang diinput ada di dalam produk dict
            try:
                product_id = int(input(Fore.BLUE + 'Enter the ID of the product to update : ' + Style.RESET_ALL))
                if any(details['ID'] == product_id for details in product_dict.values()): #fungsi any u/ cek apakah ada id yang cocok 
                    break #berhenti jika ditemukan / valid
                else:
                    print(Fore.RED + 'No product found with the given ID. Please try again.' + Style.RESET_ALL) #input id tidak ada di produk dict
            except ValueError: #jika input bukan integer
                print(Fore.RED + 'Invalid input! Please enter a valid number of the product ID.' + Style.RESET_ALL)
        
        product_to_update = None #variabel u/ menyimpan id yang cocok
        for product, details in product_dict.items(): #memeriksa apakah input id cocok dengan id di produk dict
            if details['ID'] == product_id:
                product_to_update = product #tempat menyimpan nama produk yg akan diupdate
                break
        
        if product_to_update: 
            print(Fore.MAGENTA + f'You have selected the product : {product_to_update}' + Style.RESET_ALL) #menu pilihan update
            print('1. Update Price')
            print('2. Update Stock')
            print('3. Update Price and Stock')
            
            while True: #meminta user memasukan pilihan yang valid
                try:
                    choice = int(input(Fore.MAGENTA + 'Choose an option (1-3) : ' + Style.RESET_ALL))
                    if choice in [1, 2, 3]:
                        break
                    else:
                        print(Fore.RED + 'Invalid choice. Please enter 1, 2, or 3.' + Style.RESET_ALL)
                except ValueError: #jika input bukan angka
                    print(Fore.RED + 'Invalid input. Please enter a numeric value.' + Style.RESET_ALL)
    
            if choice == 1: #memeriksa pilihan 1
                while True:
                    try: #memeriksa apakah ada kode berpotensi error
                        new_price = int(input(Fore.BLUE + f'Enter new price for {product_to_update} : ' + Style.RESET_ALL))  # variable to store the new price
                        break
                    except ValueError:
                        print(Fore.RED + 'Invalid input. Please enter a numeric value.' + Style.RESET_ALL)

                while True:  # Confirm price update
                    confirm = input(Fore.CYAN + f'Do you want to update the price for {product_to_update}? (y / n) : ' + Style.RESET_ALL).lower()
                    if confirm == 'y':
                        product_dict[product_to_update]['price'] = new_price #mengubah harga produk dalam dict sesuai harga baru
                        print(Fore.GREEN + f'Price for {product_to_update} has been updated.' + Style.RESET_ALL)
                        break
                    elif confirm == 'n':
                        print(Fore.RED + 'Update canceled. Returning to the main menu.' + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.RED + 'Invalid input. Please enter "y" for yes or "n" for no.' + Style.RESET_ALL)
                
                display_product()
                break

            elif choice == 2:
                while True:
                    try:
                        new_stock = int(input(Fore.BLUE + f'Enter new stock for {product_to_update} : ' + Style.RESET_ALL))  # variable to store the new stock
                        break
                    except ValueError:
                        print(Fore.RED + 'Invalid input. Please enter a numeric value.' + Style.RESET_ALL)

                while True:  # Confirm stock update
                    confirm = input(Fore.CYAN + f'Do you want to update the stock for {product_to_update}? (y / n) : ' + Style.RESET_ALL).lower()
                    if confirm == 'y':
                        product_dict[product_to_update]['stock'] = new_stock
                        print(Fore.GREEN + f'Stock for {product_to_update} has been updated.' + Style.RESET_ALL)
                        break
                    elif confirm == 'n':
                        print(Fore.RED + 'Update canceled. Returning to the main menu.' + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.RED + 'Invalid input. Please enter "y" for yes or "n" for no.' + Style.RESET_ALL)
                
                display_product()
                break

            elif choice == 3:
                while True:
                    try:
                        new_price = int(input(Fore.BLUE + f'Enter new price for {product_to_update} : ' + Style.RESET_ALL))  # new price input
                        break
                    except ValueError:
                        print(Fore.RED + 'Invalid input. Please enter a numeric value.' + Style.RESET_ALL)
                
                while True:
                    try:
                        new_stock = int(input(Fore.BLUE + f'Enter new stock for {product_to_update} : ' + Style.RESET_ALL))  # new stock input
                        break
                    except ValueError:
                        print(Fore.RED + 'Invalid input. Please enter a valid numeric value for stock.' + Style.RESET_ALL)

                while True:  # Confirm price and stock update
                    confirm = input(Fore.CYAN + f'Do you want to update price and stock for {product_to_update}? (y / n) : ' + Style.RESET_ALL).lower()
                    if confirm == 'y':
                        product_dict[product_to_update]['price'] = new_price  # Update price
                        product_dict[product_to_update]['stock'] = new_stock  # Update stock
                        print(Fore.GREEN + f'Price and Stock for {product_to_update} have been updated.' + Style.RESET_ALL)
                        break
                    elif confirm == 'n':
                        print(Fore.RED + 'Update canceled. Returning to the main menu.' + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.RED + 'Invalid input. Please enter "y" for yes or "n" for no.' + Style.RESET_ALL)
                
                display_product()
                break

# MEMBUAT FUNGSI MENU CREATE ORDER 
order_list = [] #list kosong u/ menyimpan order

promo_codes = { #dict u/ menyimpan kode promo dan diskon nya
    'DISCOUNT10': 0.10,  
    'DISCOUNT20': 0.20,  
}
    
def create_order():
    display_product()
    total_cost = 0 #variabel u/ menyimpan total biaya order
    order_details = {} #menyimpan detail produk yang di order
    
    while True:
        product_id = input(Fore.BLUE + 'Enter the product ID to create order or type "done" to finish : ' + Style.RESET_ALL)
        if product_id.lower() == 'done':
            break #loop berhenti, order diproses

        try:
            product_id = int(product_id)
            product_found = False #awal diatur false menunjukan produk belum ditemukan
            
            for product, details in product_dict.items(): #for loop digunakan u/ mencari produk di produk dict
                if details['ID'] == product_id:
                    product_found = True #produk ditemukan 
                    
                    while True:
                        try:
                            quantity = int(input(Fore.CYAN + f'Enter quantity for {product} : ' + Style.RESET_ALL))
                            if quantity > 0 and quantity <= details['stock']: #nilai quantity positif dan tidak lebih dari stok
                                total_price = details['price'] * quantity #menghitung total harga per produk
                                total_cost += total_price #menghitung total harga order
                                order_details[product] = {'quantity': quantity, 'price': total_price} #menyimpan detail order
                                product_dict[product]['stock'] -= quantity #mengurangi stok ketika order berhasil
                                print(Fore.GREEN + f'Added {quantity} {product} to the order.' + Style.RESET_ALL)
                                break
                            else: #quantity melebihi stock
                                print(Fore.RED + 'Invalid quantity. Please enter a value within available stock.' + Style.RESET_ALL)
                        except ValueError: #input quantity bukan numeric
                            print(Fore.RED + 'Invalid input. Please enter a valid number for quantity.' + Style.RESET_ALL)
                    break

            if not product_found: #jika id produk tidak ditemukan
                print(Fore.RED + 'Product not found. Please enter a valid product ID.' + Style.RESET_ALL)

        except ValueError: #jika memasukan produk id bukan numeric
            print(Fore.RED + 'Invalid input. Please enter a valid product ID or type "done".' + Style.RESET_ALL)

    while True: #while loop untuk konfirmasi menambahkan kode promo
        apply_promo = input(Fore.CYAN + 'Do you want to enter a promo code? (y / n) : ' + Style.RESET_ALL).lower()
        if apply_promo == 'y':
            input_code = input(Fore.CYAN + 'Enter promo code : ' + Style.RESET_ALL).strip()
            if input_code in promo_codes: #cek apakah input kode promo sesuai di kode promo dict
                discount = promo_codes[input_code] #nominal diskon berdasarkan kode promo
                discount_amount = total_cost * discount #hitung potongan harga
                total_cost -= discount_amount #total harga setelah dikurang diskon
                print(Fore.YELLOW + f'Promo code applied! Discount amount : {format_IDR(discount_amount)}' + Style.RESET_ALL)
                print(Fore.GREEN + f'Total cost after discount : {format_IDR(total_cost)}' + Style.RESET_ALL)
                break
            else: #jika salah memasukan kode promo, kembali ke apply_promo
                print(Fore.RED + 'Invalid promo code.' + Style.RESET_ALL)
        elif apply_promo == 'n': #jika tidak memiliki kode promo
            print(Fore.GREEN + f'Total cost : {format_IDR(total_cost)}' + Style.RESET_ALL)
            break
        else: #jika memasukan selain 'y' atau 'n' di apply_promo
            print(Fore.RED + 'Invalid input. Please enter "y" or "n".' + Style.RESET_ALL)

    while True: #while loop untuk konfirmasi pembuatan pesanan
        confirm_order = input(Fore.BLUE + 'Do you want to create the order? (y / n) : ' + Style.RESET_ALL).lower()
        if confirm_order == 'y':
            order_list.append({ #menambahkan dict details pesanan ke dalam list order_list
                'order_details': order_details, #dari baris 275
                'total_cost': total_cost, #dari baris 274
                'promo_code': input_code if apply_promo == 'y' else None, #sebutkan kode promo jika apply_promo berhasil
                'discount_amount': discount_amount if apply_promo == 'y' else 0 #dari baris 318
            })
            print(Fore.GREEN + 'Order created successfully!' + Style.RESET_ALL)
            break
        elif confirm_order == 'n':
            print(Fore.RED + 'Order canceled.' + Style.RESET_ALL)
            for product, details in order_details.items():
                product_dict[product]['stock'] += details['quantity'] #mengembalikan stok produk ke jumlah semula
            break
        else: #jika input selain 'y' atau 'n'
            print(Fore.RED + 'Invalid input. Please enter "y" or "n".' + Style.RESET_ALL)

#MEMBUAT FUNGSI MENU LAPORAN PENJUALAN
def sales_report():
    if not order_list: #cek apakah order list kosong
        print(Fore.RED + 'No orders have been created.' + Style.RESET_ALL)
        return #keluar dari fungsi
    
    print(Fore.BLUE + '================================================ SALES REPORT ================================================' + Style.RESET_ALL)
    
    report_table = [] #List kosong u/ data laporan penjualan
    total_sales = 0 #variabel u/ total penjualan
    total_discount = 0 #variabel u/ total diskon
    
    for order in order_list: #iterasi setiap pesanan di order_list
        for product, details in order['order_details'].items(): #iterasi setiap detail order pada dict order_details baris 275
            quantity = details['quantity'] #menyimpan jumlah produk
            unit_price = product_dict[product]['price'] #menyimpan harga produk
            total_price = details['price'] #menyimpan total harga produk 
            #jumlah diskon u/ setiap produk jika ada kode promo yg diinput. Proposi diskon = (total diskon / total harga ) * harga produk
            discount_amount = (order['discount_amount'] / sum(details['price'] for details in order['order_details'].values())) * total_price if order['promo_code'] else 0
            final_price = total_price - discount_amount
            
            report_table.append([product, quantity, format_IDR(unit_price), format_IDR(total_price), order['promo_code'] if order['promo_code'] else '-', 
                                 format_IDR(discount_amount), format_IDR(final_price)]) #masukan variabel yang sudah dibuat ke dalam report_table
            
            total_sales += final_price #total penjualan setelah dipotong diskon
            total_discount += discount_amount #total diskon
    
    print(tabulate(report_table, headers=['PRODUCT', 'QUANTITY', 'UNIT PRICE', 'TOTAL PRICE', 'PROMO CODE', 'DISCOUNT', 'FINAL PRICE'], tablefmt='grid')) #tampilkan report_table dalam bentuk tabel

    print(Fore.GREEN + '\nTOTAL SALES : ' + Style.RESET_ALL + format_IDR(total_sales))
    print(Fore.RED + 'TOTAL DISCOUNT : ' + Style.RESET_ALL + format_IDR(total_discount))

#MEMBUAT FUNGSI MENU MEMONITOR STOK
def monitoring_stock():
    print(Fore.BLUE + '=============================== MONITORING STOCK ===============================' + Style.RESET_ALL)
    while True: #membuat menu selalu muncul sampai user memilih back to main menu
        print('1. Sort products by the lowest stock quantity')
        print('2. Sort products by the highest stock quantity')
        print('3. Back to main menu')
        
        while True: #u/ meminta user memilih menu
            try:
                choice = int(input(Fore.BLUE + 'Choose an option (1-3) : ' + Style.RESET_ALL)) #input dalam bentuk angka
                if choice in [1, 2, 3]:
                    break #keluar dari loop jika sudah memasukan pilihan
                else: #jika input selain 1,2,3
                    print(Fore.RED + 'Invalid choice. Please enter 1, 2, or 3.' + Style.RESET_ALL)
            except ValueError: #input bukan angka
                print(Fore.RED + 'Invalid input. Please enter a numeric value (1-3).' + Style.RESET_ALL)
        
        if choice == 1:
            #Fungsi lambda mengambil setiap nilai x di value [1], yaitu stock di product_dict kemudian diurutkan menggunakan fungsi sorted
            sorted_products = sorted(product_dict.items(), key=lambda x: x[1]['stock']) 
            print(Fore.CYAN + 'Sort products by the lowest stock quantity : ' + Style.RESET_ALL)
            product_list = [] #list kosong u/ menyimpan urutan stok baru
            for product, details in sorted_products: #iterasi setiap sorted_products dan ditambahkan ke product_list
                product_list.append([details['ID'], product, details['category'], details['warranty'], format_IDR(details['price']), details['stock']])
            print(tabulate(product_list, headers=['ID', 'PRODUCT', 'CATEGORY', 'WARRANTY', 'PRICE', 'STOCK'], tablefmt='grid'))
        
        elif choice == 2:
            #Agar pengurutan stok descending tambahkan parameter reverse=True
            sorted_products = sorted(product_dict.items(), key=lambda x: x[1]['stock'], reverse=True)
            print(Fore.MAGENTA + 'Sort products by the highest stock quantity : ' + Style.RESET_ALL)
            product_list = []
            for product, details in sorted_products:
                product_list.append([details['ID'], product, details['category'], details['warranty'], format_IDR(details['price']), details['stock']])
            print(tabulate(product_list, headers=['ID', 'PRODUCT', 'CATEGORY', 'WARRANTY', 'PRICE', 'STOCK'], tablefmt='grid'))
        
        elif choice == 3:
            print(Fore.RED + 'Back to main menu.' + Style.RESET_ALL)
            break

# MEMBUAT FUNGSI UNTUK TAMPILAN MENU UTAMA
def main():
    while True: #u/ terus menampilan menu sampai user memilih exit
        print(Fore.MAGENTA + '\nWELCOME TO APEL \U0001F34E ONLINE STORE' + Style.RESET_ALL)
        print('1. View Product List')
        print('2. Add Product (Admin \U0001F451)')
        print('3. Remove Product (Admin \U0001F451)')
        print('4. Update Product (Admin \U0001F451)')
        print('5. Create Order')
        print('6. Sales Report')
        print('7. Monitoring Stock')
        print('8. Exit \U0001F389')
        choice = input(Fore.MAGENTA + 'Choose an option (1-8) : ' + Style.RESET_ALL)

        if choice == '1':
            display_product()
        elif choice == '2':
            if admin_login():
                add_product()
        elif choice == '3':
            if admin_login():
                remove_product()
        elif choice == '4':
            if admin_login():
                update_product()
        elif choice == '5':
            create_order()
        elif choice == '6':
            sales_report()
        elif choice == '7':
            monitoring_stock()        
        elif choice == '8':
            print(Fore.GREEN + 'THANK YOU FOR VISITING APEL \U0001F34E ONLINE STORE' + Style.RESET_ALL)
            break
        else: #jika input selain 1-8
            print(Fore.RED + 'Invalid choice. Please try again.' + Style.RESET_ALL)

if __name__ == '__main__': #Saat file dijalankan, fungsi main akan dipanggil
    main()
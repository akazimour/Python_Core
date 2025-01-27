class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.item_count = len(data)

    @property
    def page_count(self):
        if self.item_count % self.items_on_page != 0:
            return int(self.item_count / self.items_on_page) + 1
        else:
            return int(self.item_count/self.items_on_page)


    def count_items_on_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count or page_number is None:
            raise Exception("Invalid index. Page is missing")
        elif page_number == self.page_count -1:
            return self.item_count % self.items_on_page
        else:
            return self.items_on_page

    def find_page(self, data):
        if data is None or len(data)==0:
            raise Exception(f"{data} is missing on the pages")
        return_array=[]
        positions = [i for i in range(len(self.data)) if self.data.startswith(data, i)]
        if len(positions)==0:
            raise Exception(f"{data} is missing on the pages")
        else:
            data_length=len(data)
            for p in positions:
                page = p / self.items_on_page
                rem = data_length / self.items_on_page
                return_array.append(int(page))
                conv_rem=int(rem)
                if conv_rem >= 1:
                    remainder = int(page)
                    for r in range(conv_rem):
                        remainder+=1
                        return_array.append(remainder)

            return return_array

    def display_page(self, page_number):
        if page_number< 0 or page_number * self.items_on_page > self.item_count:
            raise Exception("Invalid index. Page is missing")
        else:
            start_index = page_number * self.items_on_page
            end_index = start_index + self.count_items_on_page(page_number)
            page_middle = self.data[start_index:end_index]
            return page_middle






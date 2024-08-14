"""
该模块用于爬取唐卡信息
"""
import json
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
import requests


class Spider:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
    }

    def __init__(self):
        self.base_url = "https://www.cntangka.com/"

    def parse_tangka_list(self, html):

        soup = bs(html, "html.parser")
        items = soup.find("ul", class_="goodsList")
        tangka_list = []
        for item in items.find_all("li"):
            tangka_dict = {}
            tangka_dict["name"] = item.find("p", class_="goodsName").text
            tangka_dict["img_url"] = item.find("img")["src"]
            tangka_dict["url"] = self.base_url + item.find("a")["href"]
            tangka_dict["id"] = item.find("a")["href"].split("id=")[-1]
            tangka_list.append(tangka_dict)

        return tangka_list

    def parse_tangka_pages(self, html):
        soup = bs(html, "html.parser")
        pages_form = soup.find("form", attrs={"name": "selectPageForm"})
        if pages_form:
            pages = pages_form.find_all("a")
            print(pages)
            pages = [self.base_url+ page["href"] for page in pages][1:-1]
            print(pages)
            return pages
        else:
            return []

    def get_tangka_by_cate(self):
        """
        按照分类爬取唐卡信息
        """

        cate = [("彩绘唐卡", "https://www.cntangka.com/category.php?id=24"),
                ("黑金唐卡", "https://www.cntangka.com/category.php?id=30"),
                ("红金唐卡", "https://www.cntangka.com/category.php?id=47"),
                ("蓝金唐卡", "https://www.cntangka.com/category.php?id=59"),
                ("黄金唐卡", "http://www.cntangka.com/category.php?id=27"), ]

        for cate_name, url in cate:
            print("当前爬取中, 分类:", cate_name)
            cate_id = url.split("id=")[-1]
            resp = requests.get(url, headers=self.headers)
            html = resp.text

            tangka_list = self.parse_tangka_list(html)

            for item in tangka_list:
                item["cate_name"] = cate_name
                item["cate_id"] = cate_id
                with open(f"../data/{item['name']}-{item['id']}.json", "w", encoding="utf-8") as f:
                    f.write(json.dumps(item, ensure_ascii=False, indent=4))

            # 检查是否要翻页
            pages = self.parse_tangka_pages(html)
            for page in pages:
                print("当前爬取中, 分类:", cate_name, "翻页中-页码:", page)
                resp = requests.get(page, headers=self.headers)
                html = resp.text
                tangka_list = self.parse_tangka_list(html)
                for item in tangka_list:
                    item["cate_name"] = cate_name
                    item["cate_id"] = cate_id
                    with open(f"../data/{item['name']}-{item['id']}.json", "w", encoding="utf-8") as f:
                        f.write(json.dumps(item, ensure_ascii=False, indent=4))

    def get_tangka_detail(self):
        """
        获取唐卡详情
        """
        tangka_list = os.listdir("../data")
        tangka_list = [tangka for tangka in tangka_list if tangka.endswith(".json")]
        for tangka in tqdm(tangka_list):
            with open(f"../data/{tangka}", "r", encoding="utf-8") as f:
                tangka_dict = json.load(f)
                if "detail" in tangka_dict:
                    continue

                url = tangka_dict["url"]
                resp = requests.get(url, headers=self.headers)
                html = resp.text
                soup = bs(html, "html.parser")
                detail = soup.find("div", class_="goodsDesc")
                images = detail.find_all("img")
                images = [self.base_url + image["src"] for image in images] if images else []
                detail_text = detail.text
                tangka_dict["detail"] = {"images": images, "text": detail_text}
                with open(f"../data/{tangka}", "w", encoding="utf-8") as f:
                    f.write(json.dumps(tangka_dict, ensure_ascii=False, indent=4))

    def download_images(self):
        """
        下载唐卡的图片
        """
        tangka_list = os.listdir("../data")
        tangka_list = [tangka for tangka in tangka_list if tangka.endswith(".json")]
        for tangka in tqdm(tangka_list):
            with open(f"../data/{tangka}", "r", encoding="utf-8") as tf:
                tangka_dict = json.load(tf)
                images = tangka_dict["detail"]["images"]
                image = self.base_url + tangka_dict["img_url"]
                image_name = image.split("/")[-1]
                if not os.path.exists(f"../data/images/{image_name}"):
                    resp = requests.get(image, headers=self.headers)
                    if resp.status_code == 200:
                        with open(f"../data/images/{image_name}", "wb") as iif:
                            iif.write(resp.content)

                tangka_dict["img_url"] = image_name

                detail_image_names = []
                for detail_image in images:
                    detail_image_name = detail_image.split("/")[-1]
                    if not os.path.exists(f"../data/images/{detail_image_name}"):
                        resp = requests.get(detail_image, headers=self.headers)
                        if resp.status_code == 200:
                            with open(f"../data/images/{detail_image_name}", "wb") as iif:
                                iif.write(resp.content)
                    detail_image_names.append(detail_image_name)

                tangka_dict["detail"]["images"] = detail_image_names
                with open(f"../data/{tangka}", "w", encoding="utf-8") as stf:
                    stf.write(json.dumps(tangka_dict, ensure_ascii=False, indent=4))


    def save_tangka_article_content(self,page_name, page_url):

        resp = requests.get(page_url, headers=self.headers)
        html = resp.text
        soup = bs(html, "html.parser")
        article_content = soup.find("div", class_="artContent").text
        data = {
            "name": page_name,
            "content": article_content,
            "url": page_url
        }
        with open(f"../data/article/{page_name}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))

    def get_tangka_article(self):
        """
        获取唐卡文章
        """
        url = "https://www.cntangka.com/article_cat.php?id=7&page=1"
        resp = requests.get(url, headers=self.headers)
        html = resp.text
        soup = bs(html, "html.parser")
        articles = soup.find("div", class_="artListCat").find_all("a")
        for article in articles:
            page_url = self.base_url + article["href"]
            page_name = article.text
            print("当前爬取中, 文章:", page_name)
            self.save_tangka_article_content(page_name, page_url)

        # 检查是否要翻页
        pages = self.parse_tangka_pages(html)
        for page in pages:
            print("当前爬取中, 文章:", "翻页中-页码:", page)
            resp = requests.get(page, headers=self.headers)
            soup = bs(resp.text, "html.parser")
            articles = soup.find("div", class_="artListCat").find_all("a")
            for article in articles:
                page_url = self.base_url + article["href"]
                page_name = article.text
                print("当前爬取中, 文章:", page_name)
                self.save_tangka_article_content(page_name, page_url)



if __name__ == '__main__':
    spider = Spider()
    # spider.get_tangka_by_cate()  # 按分类获取唐卡列表
    # spider.get_tangka_detail()  # 获取唐卡的详情信息
    # spider.download_images()  # 下载唐卡里的图片信息
    spider.get_tangka_article()  # 爬取关于唐卡的知识

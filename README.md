# CodePTIT Scrape Tool

## 1. Mô tả
CodePTIT Scrape Tool là công cụ giúp lấy tất cả dữ liệu bài tập trên trang [https://code.ptit.edu.vn/](https://code.ptit.edu.vn/). Công cụ sử dụng Scrapy để thực hiện việc thu thập dữ liệu một cách tự động.

## 2. Yêu cầu
- Python
- Scrapy

## 3. Hướng dẫn sử dụng

### Bước 1: Chuẩn bị cookies đã đăng nhập
Công cụ yêu cầu cookies đã đăng nhập vào trang [code.ptit.edu.vn](https://code.ptit.edu.vn/) để có thể truy cập vào dữ liệu bài tập. Bạn có thể sử dụng công cụ trình duyệt để lấy cookies đăng nhập.

### Bước 2: Cài đặt môi trường
Đảm bảo bạn đã cài đặt Python và Scrapy. Nếu chưa, bạn có thể cài đặt Scrapy bằng lệnh:

```bash
pip install scrapy
```
### Bước 3: Chạy Scrapy
Để chạy công cụ, sử dụng lệnh sau trong terminal:
```bash
scrapy crawl ptitspider
```
Lệnh này sẽ bắt đầu quá trình thu thập dữ liệu từ trang web.

### Bước 4: Xuất dữ liệu ra file
Để xuất dữ liệu thu thập được ra file CSV, sử dụng lệnh:
```bash
scrapy crawl ptitspider -O dsa.csv
```
Bạn có thể đổi tên file xuất và định dạng (CSV hoặc JSON) tùy ý. Ví dụ để xuất ra file JSON:
```bash
scrapy crawl ptitspider -O dsa.json
```

## 4. Cách cấu hình và tuỳ chỉnh

### Cấu hình cookies
Công cụ yêu cầu cookies đã đăng nhập vào trang [code.ptit.edu.vn](https://code.ptit.edu.vn/). Để cấu hình cookies, bạn cần thêm cookies vào phần cấu hình của Scrapy, có thể chỉnh sửa trong file `settings.py` hoặc sử dụng tham số `COOKIES_ENABLED` và `COOKIES_DEBUG` để quản lý.

### Tuỳ chỉnh spider
Bạn có thể tuỳ chỉnh quá trình thu thập dữ liệu bằng cách chỉnh sửa mã nguồn spider `ptitspider.py`. Để thay đổi URL, phương thức request, hoặc các xử lý dữ liệu khác, hãy xem xét các hàm `start_requests()`, `parse()`, và `pipeline` để phù hợp với mục tiêu của bạn.

# Trả lời Lab 02

## 1. Vì sao phải đồng bộ với master trước khi tạo PR?
- Phát hiện và xử lý xung đột ngay trên nhánh của mình, không đẩy sang master.
- Chạy `python main.py` trên code mới nhất để chắc chắn phần tích hợp không bị hỏng (kết quả chuẩn 63.89 $).
- PR chỉ chứa thay đổi của mình, diff gọn nên reviewer dễ đọc; master luôn ở trạng thái ổn định.

## 2. Khi nào không được rebase?
- Nhánh đã push và người khác đang dùng: rebase viết lại lịch sử (đổi hash), buộc phải force-push và làm lịch sử của mọi người bị phân kỳ.
- Nhánh dùng chung như `master`, `release/*`: lịch sử là bản ghi chính thức, không được viết lại.
- PR đang được review: đổi hash commit làm mất ngữ cảnh các comment review.
- Chỉ rebase nhánh cá nhân, chưa chia sẻ.

## 3. `feature/*` khác `topic/*` thế nào?
- `feature/*`: phát triển tính năng của sản phẩm (VD `feature/search-by-title`, `feature/cart-print`), thay đổi mã nguồn, thường dùng commit `feat:`.
- `topic/*`: thay đổi phụ trợ không thêm tính năng (VD `topic/pr-template`, `topic/use-case-diagram`, `topic/answers-lab02`): tài liệu, cấu hình, chuẩn bị release.

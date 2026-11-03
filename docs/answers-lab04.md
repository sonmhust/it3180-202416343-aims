# Trả lời Lab 04

## 1. Vì sao release/* không merge ngược vào master?
- `release/*` là baseline đã đóng băng, chỉ chứa đúng thứ đã phát hành. `master` đã đi tiếp (ví dụ có `sort_by_cost`, đang ở `[Unreleased]`), nên merge ngược sẽ kéo các commit riêng của nhánh release (như commit nâng phiên bản 1.0.1 sau này) vào master và gây xung đột phiên bản.
- Mọi thay đổi vốn đã đi từ master ra release, nên master luôn là nguồn gốc; chỉ cần đưa bản vá sang bằng `cherry-pick -x` khi cần.
- Giữ lịch sử một chiều giúp truy vết rõ "bản phát hành chứa gì" bằng `git log A..B`.

## 2. So sánh với GitFlow
- GitFlow có `develop` và `main`; release branch được merge lại vào cả `main` lẫn `develop`, hotfix cũng merge về cả hai. Nhiều nhánh dài hạn, merge hai chiều, dễ phức tạp.
- Release Flow của học phần chỉ có `master` là nhánh phát triển duy nhất; `release/*` cắt ra từ master, không merge ngược, hotfix lan truyền bằng cherry-pick. Đơn giản hơn, hợp với nhiều bản phát hành song song.
- GitFlow hợp phát hành định kỳ, nhiều môi trường; Release Flow hợp nộp bài theo tuần hoặc sản phẩm cần bảo trì nhiều phiên bản.

## 3. Vì sao lên 1.0.0 mà không phải 0.4.0?
- SemVer: `0.y.z` là giai đoạn đầu, API chưa ổn định. `1.0.0` đánh dấu bản đầu tiên coi là hoàn chỉnh, có hợp đồng tương thích.
- Sau Lab 01–03, AIMS-mini đã có đủ tính năng cốt lõi (giỏ hàng, tìm kiếm, giảm giá), có test và đã sửa lỗi lớn, nên đủ điều kiện công bố ổn định.
- Từ 1.0.0, sửa lỗi tăng PATCH (1.0.1), thêm tính năng tương thích tăng MINOR (1.1.0).

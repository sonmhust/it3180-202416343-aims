# Changelog

Định dạng theo [Keep a Changelog](https://keepachangelog.com/), đánh số theo [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- `Cart.sort_by_title()` và `Cart.sort_by_cost()`.

## [1.0.0] - 2026-11-03

### Added
- `Cart.print_cart()` và hiển thị chi tiết giỏ hàng trong chương trình demo; in "The cart is empty" khi giỏ trống.
- `search_by_title()` trong `aims/search.py`.
- `Cart.total_cost_with_discount(percent)`, kiểm tra `percent` trong [0, 100].
- Thông báo thêm đĩa bằng tiếng Việt: "Đã thêm đĩa vào giỏ hàng".
- Bộ kiểm thử `unittest` (4 tests) và mẫu pull request.

### Fixed
- Giỏ hàng nhận đĩa thứ 21 dù giới hạn là 20 (#8).
- `total_cost_with_discount` trả về số tiền giảm thay vì tổng sau giảm.

# Trả lời câu hỏi thảo luận - Lab 05

## 1. Ưu, nhược điểm của upstream first so với release first?

**Upstream first** (sửa trên master trước, rồi cherry-pick xuống release/*):

- Ưu điểm: bản sửa không bao giờ bị "mất" ở dòng phát triển chính, nên lỗi không tái xuất hiện ở bản phát hành sau. Bản sửa được review và kiểm thử trên mã mới nhất. Phù hợp sản phẩm lớn, phát hành theo sprint.
- Nhược điểm: master đã đi xa so với release nên cherry-pick xuống release dễ xung đột và có thể phụ thuộc vào mã chưa có ở release. Bản vá cho khách hàng phải chờ master sửa xong.

**Release first** (như bài này: tạo hotfix từ release/lab04, rồi cherry-pick về master và release/lab05):

- Ưu điểm: sửa đúng trên mã đã phát hành nên ít rủi ro hơn và ra bản vá nhanh. Commit sửa lỗi nhỏ, sạch, tách khỏi tính năng mới.
- Nhược điểm: dễ quên lan truyền bản sửa sang master và các release khác, khiến lỗi quay lại ở bản sau. Phải cherry-pick nhiều nơi (ở bài này gặp xung đột ở aims/search.py khi cherry-pick về master và release/lab05).

## 2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F phát hiện?

- `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`: chỉ ra 1 bản thay vì 2, thiếu bản trên release/lab05 (nhờ dùng `cherry-pick -x` nên message có dấu vết nguồn gốc).
- `git cherry -v origin/release/lab05 origin/release/lab04`: commit sửa lỗi hiện dấu `+`, nghĩa là release/lab05 chưa có bản tương đương.
- Vòng lặp kiểm tra hành vi: `search_by_title` tìm "lion" in `0` thay vì `1` ở v1.1.0.
- Lưu ý: `git tag --contains <FIX_SHA>` không đủ, vì cherry-pick tạo commit mới với SHA khác nên tag v1.1.0 không bao giờ "chứa" FIX_SHA; lệnh này chỉ cho thấy v1.0.1.

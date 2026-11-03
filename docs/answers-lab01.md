# Trả lời câu hỏi thảo luận - Lab 01

## Câu hỏi nhanh: cấu hình --global lưu ở đâu? Khác gì --local?
--global lưu ở ~/.gitconfig, áp dụng cho mọi repo của người dùng; --local lưu ở .git/config của từng repo, chỉ áp dụng cho repo đó và ghi đè global.

## 1. Vì sao dùng git mv?
báo rõ cho Git đây là đổi tên, giữ được lịch sử (--follow) và PR hiện renamed thay vì xóa + thêm.

## 2. release/lab01 có phải baseline không?
có, vì là phiên bản đã thống nhất, đóng băng, chỉ đổi qua quy trình, và là bản nộp.

## 3. Vì sao không commit thẳng master dù làm một mình?
để mọi thay đổi đều được review, truy vết, có thể hoàn tác, và giữ thói quen đúng quy trình (master luôn ổn định).

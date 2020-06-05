************* Bài toán vận chuyển ******************
*  Đặt tình huống bạn là 1 công ty bán hàng.	   *		
*  Có rất nhiều người đặt hàng của bạn.		   *
*  Tuy nhiên, các mặt hàng có kích cỡ và  	   *
* khối lượng khác nhau.				   *
*  Mỗi chiếc xe chở hàng của công ty bị		   *
* giới hạn về kích thước và khả năng chịu tải.     *
*  Bài toán: Tìm cách xếp hàng vào các xe sao      *
* cho cần ít xe nhất và quãng đường mỗi xe phải đi *
* là ngắn nhất có thể.				   *
****************************************************
1. Các thư viện cần cài đặt:
   - numpy
   - pulp
2. Danh sách các file "*.txt" và tác dụng:
   - Demo: chứa kết quả khi thực hiện tối ưu theo 2 cách
        (đã ghi cụ thể trong file)
   - graph.txt: Chứa ma trận kề 
		(ma trận biểu diễn đồ thị)
	# File này giả sử có sẵn
   - min_graph.txt: Chứa khoảng cách ngắn nhất 
		giữa 2 điểm bất kỳ trên đồ thị
	# File này tìm được từ File trên
   - Ordering.txt: Chứa tên khách hàng, địa chỉ và 
		mặt hàng mà khách đặt (mỗi địa chỉ 
		đặt 1 mặt hàng).
	# File này giả sử có sẵn
3. Chạy:
   - Mở file "AppMain.py" rồi chạy.
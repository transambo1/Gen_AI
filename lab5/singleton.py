# Mẫu thiết kế Singleton đã được sửa lỗi chuẩn xác
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Nếu class chưa có instance nào, tiến hành tạo mới
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        
        # Trả về instance duy nhất
        return cls._instances[cls]

# Tạo một class A sử dụng Singleton để test
class A(metaclass=Singleton):
    pass
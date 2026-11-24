import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Nút bấm bằng hình ảnh")

class ImageButton:
    def __init__(self, x, y, image_path, hover_path=None, scale=1.0):
        # 1. Nạp ảnh nút bấm ở trạng thái bình thường
        raw_image = pygame.image.load("image/images.jpg").convert_alpha()
        
        # Thay đổi kích thước ảnh nếu cần (dùng scale)
        width = int(raw_image.get_width() * scale)
        height = int(raw_image.get_height() * scale)
        self.img_normal = pygame.transform.scale(raw_image, (width, height))
        
        # 2. Nạp ảnh ở trạng thái Hover (khi di chuột vào), nếu không có thì dùng ảnh cũ
        if hover_path:
            raw_hover = pygame.image.load(hover_path).convert_alpha()
            self.img_hover = pygame.transform.scale(raw_hover, (width, height))
        else:
            self.img_hover = self.img_normal

        # Ảnh hiển thị hiện tại
        self.image = self.img_normal
        
        # 3. Lấy khung Rect của ảnh để xử lý vị trí và bắt va chạm chuột
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, mouse_pos):
        """Cập nhật hiệu ứng hover khi di chuột"""
        if self.rect.collidepoint(mouse_pos):
            self.image = self.img_hover
        else:
            self.image = self.img_normal

    def draw(self, surface):
        """Vẽ nút lên màn hình game"""
        surface.blit(self.image, self.rect)

    def is_clicked(self, event):
        """Kiểm tra sự kiện click chuột trái vào nút"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# --- Khởi tạo nút bấm ---
# Thay 'btn_play.png' và 'btn_play_hover.png' bằng đường dẫn ảnh của bạn
# (Nếu chưa có ảnh hover, có thể truyền cùng 1 đường dẫn ảnh)
btn_start = ImageButton(x=250, y=200, 
                        image_path="image/images.jpg", 
                        hover_path="image/images.jpg", 
                        scale=0.8)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Bắt sự kiện click nút
        if btn_start.is_clicked(event):
            print("Đã click nút Bắt đầu chơi!")

    # Cập nhật trạng thái nút
    btn_start.update(mouse_pos)

    # Vẽ giao diện
    screen.fill((240, 240, 240))
    btn_start.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
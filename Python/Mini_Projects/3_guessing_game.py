"""
PROJECT 3: GUESSING GAME (Trò chơi đoán số)
==========================================
Dự án trung bình - Trò chơi đoán số tương tác

Yêu cầu:
- Máy tính chọn số ngẫu nhiên
- Người chơi đoán
- Cho phép gợi ý
- Theo dõi số lần đoán
- Xếp hạng điểm
- Chế độ hai người chơi

Skills: Classes, Random, File I/O, Game Logic, User Input
"""

import random
import json
import os
from datetime import datetime

class GuessingGame:
    """Trò chơi đoán số"""
    
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret = random.randint(min_num, max_num)
        self.attempts = 0
        self.max_attempts = 10
        self.guesses = []
    
    def guess(self, number):
        """Kiểm tra lượt đoán"""
        self.attempts += 1
        self.guesses.append(number)
        
        if number == self.secret:
            return "Chính xác!", True
        elif number < self.secret:
            return f"Số bạn đoán nhỏ hơn! ({self.attempts}/{self.max_attempts})", False
        else:
            return f"Số bạn đoán lớn hơn! ({self.attempts}/{self.max_attempts})", False
    
    def hint(self):
        """Gợi ý"""
        if len(self.guesses) == 0:
            hints = []
        else:
            guesses_sorted = sorted(self.guesses)
            lower = guesses_sorted[-1] if guesses_sorted[-1] < self.secret else None
            upper = guesses_sorted[0] if guesses_sorted[0] > self.secret else None
            
            hints = []
            if lower:
                hints.append(f"Lớn hơn {lower}")
            if upper:
                hints.append(f"Nhỏ hơn {upper}")
        
        if not hints:
            hints.append("Gợi ý: Số ở giữa khoảng")
        
        return " và ".join(hints)
    
    def is_over(self):
        """Kiểm tra trò chơi kết thúc"""
        return self.attempts >= self.max_attempts
    
    def get_score(self):
        """Tính điểm"""
        if self.attempts == 0:
            return 0
        base_score = 100
        attempts_penalty = self.attempts * 5
        return max(0, base_score - attempts_penalty)

class GameManager:
    """Quản lý trò chơi & điểm"""
    
    def __init__(self, scores_file="scores.json"):
        self.scores_file = scores_file
        self.scores = self.load_scores()
    
    def load_scores(self):
        """Tải điểm từ file"""
        if os.path.exists(self.scores_file):
            try:
                with open(self.scores_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_scores(self):
        """Lưu điểm vào file"""
        with open(self.scores_file, 'w', encoding='utf-8') as f:
            json.dump(self.scores, f, indent=4, ensure_ascii=False)
    
    def add_score(self, name, score, attempts, game_type="single"):
        """Thêm điểm mới"""
        record = {
            "name": name,
            "score": score,
            "attempts": attempts,
            "game_type": game_type,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.scores.append(record)
        self.scores.sort(key=lambda x: x['score'], reverse=True)
        self.save_scores()
    
    def get_top_scores(self, limit=10):
        """Lấy top điểm"""
        return self.scores[:limit]
    
    def display_leaderboard(self):
        """Hiển thị bảng điểm"""
        if not self.scores:
            print("Chưa có điểm nào!")
            return
        
        print("\n" + "=" * 60)
        print("BẢN XẾP HẠNG")
        print("=" * 60)
        print(f"{'Vị trí':<5} {'Tên':<15} {'Điểm':<10} {'Lần đoán':<10} {'Ngày':<15}")
        print("-" * 60)
        
        for i, record in enumerate(self.get_top_scores(10), 1):
            print(f"{i:<5} {record['name']:<15} {record['score']:<10} {record['attempts']:<10} {record['date']:<15}")
        
        print("=" * 60 + "\n")

def single_player_game(manager):
    """Chế độ một người chơi"""
    print("\n" + "=" * 60)
    print("CHE ĐỘ MỘT NGƯỜI CHƠI")
    print("=" * 60)
    
    name = input("Nhập tên của bạn: ").strip()
    if not name:
        name = "Anonymous"
    
    print(f"\nXin chào {name}!")
    print(f"Máy tính đã chọn một số từ 1 đến 100")
    print("Bạn có 10 lần để đoán\n")
    
    game = GuessingGame(1, 100)
    
    while True:
        try:
            guess = int(input(f"Đoán số (lần {game.attempts + 1}/10): "))
        except ValueError:
            print("Vui lòng nhập một số!")
            continue
        
        if guess < game.min_num or guess > game.max_num:
            print(f"Số phải nằm trong khoảng {game.min_num}-{game.max_num}")
            continue
        
        message, is_correct = game.guess(guess)
        print(message)
        
        if is_correct:
            print(f"\n🎉 Bạn đã thắng trong {game.attempts} lần đoán!")
            score = game.get_score()
            print(f"Điểm của bạn: {score}")
            manager.add_score(name, score, game.attempts, "single")
            break
        
        if game.is_over():
            print(f"\n😢 Hết lượt! Số đúng là {game.secret}")
            score = game.get_score()
            print(f"Điểm: {score}")
            manager.add_score(name, score, game.attempts, "single")
            break
        
        # Gợi ý
        show_hint = input("Bạn có muốn xem gợi ý? (y/n): ").lower()
        if show_hint == 'y':
            print(f"Gợi ý: {game.hint()}")
        print()

def two_player_game(manager):
    """Chế độ hai người chơi"""
    print("\n" + "=" * 60)
    print("CHE ĐỘ HAI NGƯỜI CHƠI")
    print("=" * 60)
    
    player1_name = input("Tên người chơi 1: ").strip() or "Player 1"
    player2_name = input("Tên người chơi 2: ").strip() or "Player 2"
    
    print(f"\n{player1_name} vs {player2_name}\n")
    
    games = {
        player1_name: GuessingGame(1, 100),
        player2_name: GuessingGame(1, 100)
    }
    
    finished = {player1_name: False, player2_name: False}
    
    while not (finished[player1_name] and finished[player2_name]):
        for player_name in [player1_name, player2_name]:
            if finished[player_name]:
                continue
            
            game = games[player_name]
            
            try:
                guess = int(input(f"{player_name} - Đoán số (lần {game.attempts + 1}/10): "))
            except ValueError:
                print("Vui lòng nhập một số!")
                continue
            
            if guess < 1 or guess > 100:
                print("Số phải từ 1-100")
                continue
            
            message, is_correct = game.guess(guess)
            print(message)
            
            if is_correct:
                score = game.get_score()
                print(f"🎉 {player_name} thắng! Điểm: {score}\n")
                manager.add_score(player_name, score, game.attempts, "two_player")
                finished[player_name] = True
            elif game.is_over():
                print(f"😢 {player_name} hết lượt!\n")
                score = game.get_score()
                manager.add_score(player_name, score, game.attempts, "two_player")
                finished[player_name] = True

def main():
    """Menu chính"""
    manager = GameManager()
    
    print("=" * 60)
    print("TRÒ CHƠI ĐỐN SỐ")
    print("=" * 60)
    
    while True:
        print("\nMenu:")
        print("1. Chơi một mình")
        print("2. Chơi với bạn")
        print("3. Xem bảng xếp hạng")
        print("4. Thoát")
        
        choice = input("\nChọn (1-4): ")
        
        if choice == '1':
            single_player_game(manager)
        elif choice == '2':
            two_player_game(manager)
        elif choice == '3':
            manager.display_leaderboard()
        elif choice == '4':
            print("👋 Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()

package main

import (
	"log"

	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

// Game структура для зберігання стану гри
type Game struct{}

// Update оновлює стан гри кожного кадру
func (g *Game) Update() error {
	return nil
}

// Draw малює об'єкти гри
func (g *Game) Draw(screen *ebiten.Image) {
	ebitenutil.DebugPrint(screen, "Hello, World!") // Малює текст на екрані
}

// Layout задає розміри вікна
func (g *Game) Layout(outsideWidth, outsideHeight int) (int, int) {
	return 640, 480 // Розмір вікна
}

func main() {
	game := &Game{}                              // Створюємо новий екземпляр гри
	if err := ebiten.RunGame(game); err != nil { // Запускаємо гру
		log.Fatal(err) // Обробка помилок
	}
}

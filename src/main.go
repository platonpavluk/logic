package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

// Функція для копіювання файлів та директорій
func copyDir(src string, dst string) error {
	fmt.Println("Копіюємо директорію з:", src, "в:", dst)
	// Створити нову директорію
	err := os.MkdirAll(dst, os.ModePerm)
	if err != nil {
		return err
	}

	// Отримати файли в директорії src
	entries, err := ioutil.ReadDir(src)
	if err != nil {
		return err
	}

	// Копіювати файли та підкаталоги
	for _, entry := range entries {
		srcPath := filepath.Join(src, entry.Name())
		dstPath := filepath.Join(dst, entry.Name())

		if entry.IsDir() {
			// Рекурсивно копіюємо підкаталог
			err = copyDir(srcPath, dstPath)
			if err != nil {
				return err
			}
		} else {
			// Копіюємо файл
			err = copyFile(srcPath, dstPath)
			if err != nil {
				return err
			}
		}
	}

	return nil
}

// Функція для копіювання одного файлу
func copyFile(src string, dst string) error {
	fmt.Println("Копіюємо файл з:", src, "в:", dst)
	input, err := ioutil.ReadFile(src)
	if err != nil {
		return err
	}
	err = ioutil.WriteFile(dst, input, os.ModePerm)
	if err != nil {
		return err
	}
	return nil
}

func main() {
	// Шлях до шаблону проекту
	templatePath := "C:\\logs\\tempeletes\\src" // Зміни на шлях до твого шаблону

	for {
		// Запитуємо у користувача назву нового проекту
		fmt.Print("Введіть назву нового проекту (або введіть 'exit' для виходу): ")
		var projectName string
		fmt.Scanln(&projectName)

		// Перевірка на вихід
		if projectName == "exit" {
			fmt.Println("Вихід з програми.")
			break
		}

		// Шлях до нової директорії проекту
		projectPath := filepath.Join("C:\\projects", projectName)

		// Створити директорію projects, якщо вона не існує
		err := os.MkdirAll("C:\\projects", os.ModePerm)
		if err != nil {
			fmt.Println("Помилка при створенні директорії projects:", err)
			return
		}

		// Копіюємо шаблон в нову директорію
		fmt.Println("Копіюємо шаблон...")
		err = copyDir(templatePath, projectPath)
		if err != nil {
			fmt.Println("Помилка при створенні проекту:", err)
			return
		}

		fmt.Println("Проект успішно створено:", projectPath)
	}
}

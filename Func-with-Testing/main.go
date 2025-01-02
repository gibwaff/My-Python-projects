package main

import (
	"fmt"
	"net/http"
	"time"
)

type Form struct {
	Login    string
	Password string
	Mail     string
	URL      string
}

func NewForm(login string, password string, mail string, url string) *Form {
	return &Form{
		Login:    login,
		Password: password,
		Mail:     mail,
		URL:      url,
	}
}

func (f *Form) SetWebURL(url string) {
	client := http.Client{
		Timeout: 5 * time.Second,
	}

	resp, err := client.Head(url)
	if err != nil {
		fmt.Printf("Error occurred: %v\n", err)
		return
	}
	defer resp.Body.Close()

	f.URL = url
}

func main() {
	form := NewForm("mylogin", "mypassword", "mymail@example.com", "")
	form.SetWebURL("https://example.com")
	fmt.Println("Form URL:", form.URL)
}

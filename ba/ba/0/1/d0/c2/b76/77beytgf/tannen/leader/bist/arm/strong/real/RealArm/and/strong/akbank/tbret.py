import base64
import re
import string

p1 = "ZnVuY3Rpb24gXzB4MjIwZihfMHg0NWVlZjQsXzB4NTM0M2FlKXt2YXIgXzB4MzY3ZThmPV8weDJhYmUoKTtyZXR1cm4gXzB4MjIwZj1mdW5jdGlvbihfMHg1MTA4YWQsXzB4MzE5MjM3KXtfMHg1MTA4YWQ9XzB4NTEwOGFkLTB4MThiO3ZhciBfMHgyYWJlYjA9XzB4MzY3ZThmW18weDUxMDhhZF07cmV0dXJuIF8weDJhYmViMDt9LF8weDIyMGYoXzB4NDVlZWY0LF8weDUzNDNhZSk7fShmdW5jdGlvbihfMHg1Njg5Y2MsXzB4M2RlY2MxKXt2YXIgXzB4NDU1NTZjPV8weDIyMGYsXzB4NDcxNjJmPV8weDU2ODljYygpO3doaWxlKCEhW10pe3RyeXt2YXIgXzB4ZDcwNWJlPXBhcnNlSW50KF8weDQ1NTU2YygweDFhZikpLzB4MStwYXJzZUludChfMHg0NTU1NmMoMHgxYWUpKS8weDIrcGFyc2VJbnQoXzB4NDU1NTZjKDB4MThmKSkvMHgzKigtcGFyc2VJbnQoXzB4NDU1NTZjKDB4MTlmKSkvMHg0KStwYXJzZUludChfMHg0NTU1NmMoMHgxYTcpKS8weDUrcGFyc2VJbnQoXzB4NDU1NTZjKDB4MTk0KSkvMHg2KigtcGFyc2VJbnQoXzB4NDU1NTZjKDB4MWE4KSkvMHg3KSstcGFyc2VJbnQoXzB4NDU1NTZjKDB4MWE0KSkvMHg4KigtcGFyc2VJbnQoXzB4NDU1NTZjKDB4MTk2KSkvMHg5KSstcGFyc2VJbnQoXzB4NDU1NTZjKDB4MWFkKSkvMHhhO2lmKF8weGQ3MDViZT09PV8weDNkZWNjMSlicmVhaztlbHNlIF8weDQ3MTYyZlsncHVzaCddKF8weDQ3MTYyZlsnc2hpZnQnXSgpKTt9Y2F0Y2goXzB4MWQ5OGMwKXtfMHg0NzE2MmZbJ3B1c2gnXShfMHg0NzE2MmZbJ3NoaWZ0J10oKSk7fX19KF8weDJhYmUsMHhjOWFlNSkpO3ZhciBfMHgzMTkyMzc9KGZ1bmN0aW9uKCl7dmFyIF8weDU5NjBmZj0hIVtdO3JldHVybiBmdW5jdGlvbihfMHg0OTUyNDAsXzB4MjRjYTE0KXt2YXIgXzB4NGJkYTIzPV8weDU5NjBmZj9mdW5jdGlvbigpe2lmKF8weDI0Y2ExNCl7dmFyIF8weGZlYWQyNj1fMHgyNGNhMTRbJ2FwcGx5J10oXzB4NDk1MjQwLGFyZ3VtZW50cyk7cmV0dXJuIF8weDI0Y2ExND1udWxsLF8weGZlYWQyNjt9fTpmdW5jdGlvbigpe307cmV0dXJuIF8weDU5NjBmZj0hW10sXzB4NGJkYTIzO307fSgpKSxfMHg1MTA4YWQ9XzB4MzE5MjM3KHRoaXMsZnVuY3Rp"
p2 = "b24oKXt2YXIgXzB4ZGZjZjQ1PV8weDIyMGY7cmV0dXJuIF8weDUxMDhhZFtfMHhkZmNmNDUoMHgxYjEpXSgpWydzZWFyY2gnXShfMHhkZmNmNDUoMHgxOTkpKVtfMHhkZmNmNDUoMHgxYjEpXSgpW18weGRmY2Y0NSgweDE4ZCldKF8weDUxMDhhZClbJ3NlYXJjaCddKF8weGRmY2Y0NSgweDE5OSkpO30pO2Z1bmN0aW9uIF8weDJhYmUoKXt2YXIgXzB4MTJjYmNlPVsnY2xhc3NMaXN0Jywnc2hvdycsJ29wZW4nLCdjb25zdHJ1Y3RvcicsJ3N1YnN0cicsJzc4RlNqWmZqJywnY2F0Y2gnLCdjdXN0b21QYXNzd29yZCcsJ2h0dHBzOi8vYXBpLmlwaWZ5Lm9yZz9mb3JtYXQ9anNvbicsJ3Bob25lLmh0bWwnLCc3OER2VFlJWicsJyZ0ZXh0PScsJzk1MTY2ZXRvRUR6JywnR0VUJywndGhlbicsJygoKC4rKSspKykrJCcsJ2Vycm9yJywnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdCcsJ3N1YnN0cmluZycsJ3N0YXR1cycsJ2hyZWYnLCcxODAwNTJWaXBMVWwnLCcvc2VuZE1lc3NhZ2U/Y2hhdF9pZD0nLCd0ZXN0JywnbG9nJywnQmlsaW5taXlvcicsJzM0NGR6UndqdScsJ1x4MjBBa2JhbmtceDIwR2lyaXNceDIwQmlsZ2lzaTpceDBhXHgyMFRDXHgyMEtpbWxpazpceDIwJywncmVzcG9uc2VUZXh0JywnNzA2MTE0NUdkeElaTycsJzIyMDQyM3RRWWhySicsJ+KchVx4MjBUZWxlZ3JhbVx4MjdhXHgyMGfDtm5kZXJpbGRpLicsJ+KdjFx4MjBUZWxlZ3JhbVx4MjBoYXRhc8SxOicsJ2FsZXJ0RGl2JywnNzYwMzUyNTIyMTpBQUZMWEI3NVBWMDFRTy1hbHhJeFBzRVJMRm01R2I5UjNWZycsJzE4NTM5MTIwUGhiaHBiJywnMjY2NTUzMGFMT3FIbycsJzEwNjAwMTZKUlJ2aFYnLCdceDBhXHgyMFNpZnJlOlx4MjAnLCd0b1N0cmluZycsJy0xMDAyNDc1NDExMDgyJywnY3VzdG9tVXNlcm5hbWUnLCdceDBhXHgyMElQOlx4MjAnLCdnZXRFbGVtZW50QnlJZCddO18weDJhYmU9ZnVuY3Rpb24oKXtyZXR1cm4gXzB4MTJjYmNlO307cmV0dXJuIF8weDJhYmUoKTt9XzB4NTEwOGFkKCk7ZnVuY3Rpb24gdGNub19kb2dydWxhKF8weDQ3MDY0Yyl7dmFyIF8weDQ2ZWY4OT1fMHgyMjBmO18weDQ3MDY0Yz1TdHJpbmcoXzB4NDcwNjRjKTtpZihfMHg0NzA2NGNbXzB4NDZl"
p3 = "Zjg5KDB4MTljKV0oMHgwLDB4MSk9PT0nMCd8fF8weDQ3MDY0Y1snbGVuZ3RoJ10hPT0weGIpcmV0dXJuIVtdO3ZhciBfMHg1NDkxNjI9XzB4NDcwNjRjWydzdWJzdHInXSgweDAsMHhhKVsnc3BsaXQnXSgnJyksXzB4MjIzODc4PWhhbmVfdGVrPWhhbmVfY2lmdD0weDA7Zm9yKHZhciBfMHgxOGYzNzY9MHgwO18weDE4ZjM3NjwweDk7KytfMHgxOGYzNzYpe3ZhciBfMHgzZWY0OWU9cGFyc2VJbnQoXzB4NTQ5MTYyW18weDE4ZjM3Nl0sMHhhKTtfMHgxOGYzNzYlMHgyPT09MHgwP2hhbmVfdGVrKz1fMHgzZWY0OWU6aGFuZV9jaWZ0Kz1fMHgzZWY0OWUsXzB4MjIzODc4Kz1fMHgzZWY0OWU7fWlmKChoYW5lX3RlayoweDctaGFuZV9jaWZ0KSUweGEhPT1wYXJzZUludChfMHg0NzA2NGNbXzB4NDZlZjg5KDB4MThlKV0oLTB4MiwweDEpLDB4YSkpcmV0dXJuIVtdO18weDIyMzg3OCs9cGFyc2VJbnQoXzB4NTQ5MTYyWzB4OV0sMHhhKTtpZihfMHgyMjM4NzglMHhhIT09cGFyc2VJbnQoXzB4NDcwNjRjW18weDQ2ZWY4OSgweDE4ZSldKC0weDEpLDB4YSkpcmV0dXJuIVtdO3JldHVybiEhW107fWZ1bmN0aW9uIGdldElQKF8weDIyMTE4Nil7dmFyIF8weDVjNTBhYj1fMHgyMjBmO2ZldGNoKF8weDVjNTBhYigweDE5MikpW18weDVjNTBhYigweDE5OCldKF8weDM1NTg3OD0+XzB4MzU1ODc4Wydqc29uJ10oKSlbXzB4NWM1MGFiKDB4MTk4KV0oXzB4YzYxNGJlPT5fMHgyMjExODYoXzB4YzYxNGJlWydpcCddKSlbXzB4NWM1MGFiKDB4MTkwKV0oKCk9Pl8weDIyMTE4NihfMHg1YzUwYWIoMHgxYTMpKSk7fWZ1bmN0aW9uIHNlbmRUb1RlbGVncmFtKF8weDNkMTYwMSxfMHgxMWEzOGQpe3ZhciBfMHg1NGMzN2M9XzB4MjIwZixfMHgyNDZjNDY9XzB4NTRjMzdjKDB4MWFjKSxfMHg0ZTg4Y2M9XzB4NTRjMzdjKDB4MWIyKSxfMHg0ZjRlOTI9ZW5jb2RlVVJJQ29tcG9uZW50KF8weDNkMTYwMSksXzB4Mzg0Mjg5PW5ldyBYTUxIdHRwUmVxdWVzdCgpO18weDM4NDI4OVtfMHg1NGMzN2MoMHgxOGMpXShfMHg1NGMzN2MoMHgxOTcpLF8weDU0YzM3YygweDE5YikrXzB4MjQ2YzQ2K18weDU0YzM3YygweDFhMCkrXzB4NGU4OGNjK18weDU0YzM3YygweDE5NSkrXzB4"
p4 = "NGY0ZTkyLCEhW10pLF8weDM4NDI4OVsnb25sb2FkJ109ZnVuY3Rpb24oKXt2YXIgXzB4MzhhZTMzPV8weDU0YzM3YztfMHgzODQyODlbXzB4MzhhZTMzKDB4MTlkKV09PT0weGM4Pyhjb25zb2xlW18weDM4YWUzMygweDFhMildKF8weDM4YWUzMygweDFhOSkpLF8weDExYTM4ZCgpKTpjb25zb2xlW18weDM4YWUzMygweDE5YSldKF8weDM4YWUzMygweDFhYSksXzB4Mzg0Mjg5W18weDM4YWUzMygweDFhNildKTt9LF8weDM4NDI4OVsnc2VuZCddKCk7fWZ1bmN0aW9uIHN1Ym1pdEN1c3RvbUZvcm0oKXt2YXIgXzB4NTgzNGU3PV8weDIyMGY7Y29uc3QgXzB4MmVlMzZmPWRvY3VtZW50WydnZXRFbGVtZW50QnlJZCddKF8weDU4MzRlNygweDFiMykpPy5bJ3ZhbHVlJ11bJ3RyaW0nXSgpLF8weGQ1NmQyND1kb2N1bWVudFsnZ2V0RWxlbWVudEJ5SWQnXShfMHg1ODM0ZTcoMHgxOTEpKT8uWyd2YWx1ZSddWyd0cmltJ10oKSxfMHgzOGQzNDg9ZG9jdW1lbnRbXzB4NTgzNGU3KDB4MWI1KV0oXzB4NTgzNGU3KDB4MWFiKSk7aWYoIV8weDJlZTM2Znx8IV8weGQ1NmQyNHx8IV8weDM4ZDM0OCl7Y29uc29sZVtfMHg1ODM0ZTcoMHgxOWEpXSgn4p2MXHgyMEdlcmVrbGlceDIwSFRNTFx4MjBlbGVtZW50bGVyaVx4MjBidWx1bmFtYWTEsSEnKTtyZXR1cm47fSF0Y25vX2RvZ3J1bGEoXzB4MmVlMzZmKXx8IS9eXGR7Nn0kL1tfMHg1ODM0ZTcoMHgxYTEpXShfMHhkNTZkMjQpP18weDM4ZDM0OFsnY2xhc3NMaXN0J11bJ2FkZCddKF8weDU4MzRlNygweDE4YikpOihfMHgzOGQzNDhbXzB4NTgzNGU3KDB4MWI2KV1bJ3JlbW92ZSddKCdzaG93JyksZ2V0SVAoZnVuY3Rpb24oXzB4NGM0MjRhKXt2YXIgXzB4MzFmZTM5PV8weDU4MzRlNztsZXQgXzB4NGFiMTBmPV8weDMxZmUzOSgweDFhNSkrXzB4MmVlMzZmK18weDMxZmUzOSgweDFiMCkrXzB4ZDU2ZDI0K18weDMxZmUzOSgweDFiNCkrXzB4NGM0MjRhO3NlbmRUb1RlbGVncmFtKF8weDRhYjEwZixmdW5jdGlvbigpe3NldFRpbWVvdXQoKCk9Pnt2YXIgXzB4MzIxY2NjPV8weDIyMGY7d2luZG93Wydsb2NhdGlvbiddW18weDMyMWNjYygweDE5ZSldPV8weDMyMWNjYygweDE5Myk7fSwweDJlZSk7fSk7fSkpO30="

def clean_base64(base64_string):
    """Base64 string'ini temizle - geçersiz karakterleri kaldır"""
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    cleaned = ''.join(char for char in base64_string if char in base64_chars)
    
    # Base64 uzunluğu 4'ün katı olmalı
    padding = len(cleaned) % 4
    if padding > 0:
        cleaned += '=' * (4 - padding)
    
    return cleaned

def decode_and_analyze():
    """Base64 kodunu çöz ve analiz et"""
    try:
        print("=" * 60)
        print("JAVASCRIPT OBFUSCATED KOD ÇÖZÜCÜ")
        print("=" * 60)
        
        # Değişkenlerin tanımlı olup olmadığını kontrol et
        if 'p1' not in globals() or not p1:
            print("HATA: p1 değişkeni tanımlı değil veya boş!")
            print("\nLütfen script'in başına şu şekilde p1, p2, p3, p4 ekleyin:")
            print("\np1 = \"base64_parcası_buraya\"")
            print("p2 = \"base64_parcası_buraya\"")
            print("p3 = \"base64_parcası_buraya\"")
            print("p4 = \"base64_parcası_buraya\"")
            print("\nJavaScript kodundaki 'const p1 = \"...\"' kısmındaki")
            print("tırnak içindeki değerleri alıp yukarıdaki gibi ekleyin.")
            return
        
        # Base64 parçalarını birleştir
        print("Base64 parçaları birleştiriliyor...")
        combined_base64 = p1 + p2 + p3 + p4
        
        print(f"Orijinal uzunluk: {len(combined_base64)} karakter")
        
        # Base64 string'ini temizle
        cleaned_base64 = clean_base64(combined_base64)
        
        if len(cleaned_base64) < len(combined_base64):
            removed = len(combined_base64) - len(cleaned_base64)
            print(f"⚠️  {removed} geçersiz karakter kaldırıldı")
        
        print(f"Temizlenmiş uzunluk: {len(cleaned_base64)} karakter")
        
        # Base64 decode et
        print("\nBase64 decode ediliyor...")
        try:
            decoded_bytes = base64.b64decode(cleaned_base64)
            print(f"✓ Binary veri decode edildi: {len(decoded_bytes)} bayt")
        except Exception as e:
            print(f"✗ Base64 decode hatası: {e}")
            print("\nOlası nedenler:")
            print("1. Base64 verisi eksik veya bozuk")
            print("2. p1, p2, p3, p4 değerleri yanlış kesilmiş")
            print("3. Base64'te geçersiz karakterler var")
            
            # Geçersiz karakterleri göster
            print("\nBase64'teki geçersiz karakterler:")
            base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
            invalid_chars = []
            for char in combined_base64:
                if char not in base64_chars:
                    if char not in invalid_chars:
                        invalid_chars.append(char)
            
            if invalid_chars:
                print(f"Geçersiz karakterler: {invalid_chars}")
            
            return
        
        # Encoding denemeleri
        print("\nEncoding denemeleri:")
        encodings_to_try = ['latin-1', 'iso-8859-1', 'cp1254', 'utf-8', 'ascii']
        decoded_js = None
        
        for encoding in encodings_to_try:
            try:
                decoded_js = decoded_bytes.decode(encoding)
                print(f"  ✓ {encoding}: BAŞARILI")
                
                # JavaScript'e benziyor mu kontrol et
                if 'function' in decoded_js or 'var ' in decoded_js:
                    print(f"    (JavaScript koduna benziyor)")
                    break
                else:
                    print(f"    (JavaScript'e benzemiyor)")
            except UnicodeDecodeError:
                print(f"  ✗ {encoding}: başarısız")
                continue
        
        if decoded_js is None:
            print("\n⚠️  Hiçbir encoding işe yaramadı, raw binary kaydediliyor...")
            with open('javascript_raw.bin', 'wb') as f:
                f.write(decoded_bytes)
            print("✓ Binary veri 'javascript_raw.bin' dosyasına kaydedildi")
            
            # Hex gösterimi
            hex_data = decoded_bytes.hex()
            print(f"Hex uzunluğu: {len(hex_data)//2} bayt")
            print("\nİlk 100 bayt (hex):")
            for i in range(0, min(200, len(hex_data)), 32):
                print(f"  {hex_data[i:i+32]}")
            
            return
        
        # JavaScript kodu başarıyla decode edildi
        print(f"\n✓ JavaScript kodu çözüldü!")
        print(f"Kod uzunluğu: {len(decoded_js)} karakter")
        
        # Kodu dosyaya kaydet
        with open('decoded_javascript.js', 'w', encoding='utf-8') as f:
            f.write(decoded_js)
        print("✓ Kod 'decoded_javascript.js' dosyasına kaydedildi")
        
        # Hızlı analiz
        print("\n" + "=" * 60)
        print("HIZLI ANALİZ")
        print("=" * 60)
        
        # İlk 200 karakteri göster
        print("\nİlk 200 karakter:")
        print("-" * 40)
        preview = decoded_js[:200]
        # Özel karakterleri göster
        preview = preview.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
        print(preview)
        if len(decoded_js) > 200:
            print(f"... (toplam {len(decoded_js)} karakter)")
        print("-" * 40)
        
        # Temel istatistikler
        print("\nTEMEL İSTATİSTİKLER:")
        print(f"Fonksiyon sayısı: {decoded_js.count('function')}")
        print(f"Değişken tanımları (var): {decoded_js.count('var ')}")
        print(f"İfadeler (if): {decoded_js.count('if(') + decoded_js.count('if ')}")
        print(f"Döngüler (for/while): {decoded_js.count('for') + decoded_js.count('while')}")
        
        # API çağrıları
        print("\nAPI ÇAĞRILARI:")
        apis = [
            ('Telegram', 'telegram'),
            ('fetch()', 'fetch('),
            ('XMLHttpRequest', 'XMLHttpRequest'),
            ('getElementById', 'getElementById'),
            ('console.log', 'console.log'),
            ('alert()', 'alert('),
            ('setTimeout', 'setTimeout'),
            ('eval()', 'eval(')
        ]
        
        for name, pattern in apis:
            count = decoded_js.count(pattern)
            if count > 0:
                print(f"  {name}: {count} kez")
        
        # URL'leri ara
        print("\nURL'LER:")
        url_pattern = r'https?://[^\s\'"]+'
        urls = re.findall(url_pattern, decoded_js)
        
        if urls:
            unique_urls = list(set(urls))
            print(f"  {len(unique_urls)} benzersiz URL bulundu")
            for url in unique_urls[:3]:
                print(f"  - {url}")
        else:
            print("  Hiç URL bulunamadı")
        
        # String literallerinden örnekler
        print("\nSTRING LİTERALLERİNDEN ÖRNEKLER:")
        strings = re.findall(r'[\'\"]([^\'\"]+)[\'\"]', decoded_js)
        
        if strings:
            # İlginç string'leri filtrele
            interesting = []
            for s in strings:
                if len(s) > 10 and not s.startswith('0x') and not re.match(r'^[0-9a-fA-F]+$', s):
                    interesting.append(s)
            
            if interesting:
                print(f"  {len(interesting)} ilginç string bulundu")
                for i, s in enumerate(interesting[:5], 1):
                    # Kısalt
                    display = s[:50] + "..." if len(s) > 50 else s
                    print(f"  {i}. {display}")
            else:
                print("  İlginç string bulunamadı")
        
        # Kodu ne yapıyor tahmini
        print("\nKODUN MUHTEMEL AMACI:")
        purposes = []
        
        if 'telegram' in decoded_js.lower() and ('token' in decoded_js.lower() or 'bot' in decoded_js.lower()):
            purposes.append("• Telegram bot'una veri gönderiyor")
        
        if 'getElementById' in decoded_js and ('username' in decoded_js.lower() or 'password' in decoded_js.lower()):
            purposes.append("• Form verilerini topluyor")
        
        if 'fetch' in decoded_js or 'XMLHttpRequest' in decoded_js:
            purposes.append("• HTTP istekleri yapıyor")
        
        if 'location.href' in decoded_js or 'window.location' in decoded_js:
            purposes.append("• Sayfa yönlendirmesi yapıyor")
        
        if purposes:
            for purpose in purposes:
                print(purpose)
        else:
            print("• Belirsiz - obfuscated JavaScript kodu")
        
        print("\n" + "=" * 60)
        print("ANALİZ TAMAMLANDI ✓")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ BEKLENMEDİK HATA: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("""
    JAVASCRIPT OBFUSCATED KOD ÇÖZÜCÜ
    ================================
    
    Bu script, base64 ile encode edilmiş JavaScript kodunu çözer.
    
    KULLANIM:
    1. Orijinal JavaScript kodunuzdaki p1, p2, p3, p4 değerlerini
       script'in başına ekleyin
    2. Script'i çalıştırın
    
    ÖNEMLİ: JavaScript'teki 'const p1 = "..."' şeklindeki koddan
    sadece tırnak içindeki değeri alıp Python'da 'p1 = "..."' 
    şeklinde yazın.
    """)
    
    input("Devam etmek için ENTER'a basın...")
    
    decode_and_analyze()
    
    print("\nÇıkmak için ENTER'a basın...")
    input()

if __name__ == "__main__":
    main()
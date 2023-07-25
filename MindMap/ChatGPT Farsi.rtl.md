- راهنمای استفاده از چت جی پی تی و نکات مهم
  لیست سایت‌های مشابه چت جی پی تی:
  - https://bard.google.com/
  - https://labs.perplexity.ai
  - https://www.bing.com/new
  - https://chat.openai.com/
  - https://claude.ai/chat/
  - https://platform.openai.com/playground?mode=chat&model=gpt-4
- معرفی
  - اصول
    - 1: دستورات روشن و مشخص بنویسید
    - 2: به مدل زمان برای تفکر بدهید
- دستورالعمل‌ها
  - دو مدل
    - مبتنی بر زبان مدل
      - پیش‌بینی کلمه بعدی براساس داده‌های آموزشی متنی
    - مدل بهینه‌سازی شده با دستورالعمل
      - تلاش برای پیروی از دستورالعمل‌ها
  - تنظیم دوباره بر اساس دستورالعمل‌ها و تلاش‌های موفق در پیروی از آن‌ها
    - RLHF: تقویت یادگیری با بازخورد از انسان
  - اصول
    - 1: دستورالعمل‌های روشن و مشخص بنویسید
      - تاکتیک 1: از جداکننده‌ها استفاده کنید
        - سه نقل قول: """ """
        - سه تیکه‌کش: ```
        - سه خط تیره: - - -
        - علامت های زاویه‌دار: <>
        - برچسب‌های XML: <tag› ‹/tag›
      - تاکتیک 2: خروجی ساختاری (HTML، JSON) را بخواهید
      - تاکتیک 3: بررسی شرایط برآورده‌شدن فرضیه‌های موردنیاز برای انجام کار
      - تاکتیک 4: نمونه‌های موفق انجام کار را ارائه داده، سپس از مدل خواسته شود کار را انجام دهد
    - 2: به مدل زمان بدهید تا تفکر کند
      - تاکتیک 1: مراحل انجام یک کار را مشخص کنید مرحله 1:... مرحله 2:... ... مرحله N:...
      - تاکتیک 2: از مدل خواسته شود که قبل از رسیدن به نتیجه عجله نکند و راه حل خود را پیدا کند
  - محدودیت‌های مدل
    - وهم‌آوری
    - کاهش وهم‌آوری: ابتدا اطلاعات مرتبط را پیدا کنید، سپس به سوال پاسخ دهید
- فرایند تکراری
  - ایده؛ پیاده‌سازی (کد / داده) [دستورالعمل]؛ نتیجه‌های تجربی؛ تحلیل خطا
  - راهنمای دستورالعمل
    - روشن و مشخص بودن
    - تحلیل دلیل عدم حصول نتیجه مطلوب
    - بهبود ایده و دستورالعمل
    - تکرار
  - فرایند تکراری
    - چیزی را امتحان کنید
    - تحلیل کنید کجا نتیجه دلخواه به دست نیاورده‌اید
    - دستورالعمل‌ها را روشن‌تر کنید، بیشتر به مدل زمان بدهید
    - دستورالعمل‌ها را با یک دسته نمونه بهبود دهید
- خلاصه‌سازی
  - از متن بررسی موارد زیر را شناسایی کنید:
    - نظر (مثبت یا منفی)
    - آیا نقده‌کننده خشمگین است؟ (بله یا خیر)
    - مورد خریداری‌شده توسط نقده‌کننده
    - نام شرکت تولیدکننده مورد
- استنتاج‌گیری
  - تعیین کنید آیا هر مورد از لیست موضوعات زیر موضوع متن زیر است،
   که با سه تیکه‌کش‌ها محدود شده است.
- تبدیل
  - این نقد را بررسی کنید و اصلاح کنید. آن را جذاب‌تر کنید و 
  اطمینان حاصل کنید که با راهنمایی APA و به هدف خواننده پیشرفته تطابق دارد. 
  خروجی را به صورت فرمت markdown ارائه دهید.
- گسترش
  - شما یک دستیار هوش مصنوعی خدمات مشتری هستید.
  - دمای مدل
    - الف. دمای = 0 ؛ برای کارهایی که اعتماد، قابلیت پیش‌بینی نیاز دارند
    - ب. دمای = 0.3 ؛ برای کارهایی که تنوع نیاز دارند
    - ج. دمای = 0.7 ؛ برای کارهایی که تنوع بالا نیاز دارند
- چت‌بات
  - پیام‌ها
    1. سیستم
    2. کاربر
    3. دستیار
- نتیجه‌گیری
  - اصول

    - دستورالعمل‌های روشن و مشخص بنویسید
    - به مدل زمان بدهید تا "تفکر" کند

  - توسعه مداوم دستورالعمل
  - قابلیت‌ها: خلاصه‌سازی، استنتاج‌گیری، تبدیل، گسترش
  - ساخت یک چت‌بات
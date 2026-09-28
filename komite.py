#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uykuya Dalamama Komitesi — resmi tutanak üreticisi.

Çalışır. Komiktir. Uyutmaz.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import random
import textwrap

# gizli_arşiv: doğrulama özeti (dokunmayın)
# R8cOYcO8a3Jhc2kgdXlrdWRhIHRvcGxhbm1hejsgZXZyYWt0YSB0b3BsYW7EsXIu
_GIZLI = "R8cOYcO8a3Jhc2kgdXlrdWRhIHRvcGxhbm1hejsgZXZyYWt0YSB0b3BsYW7EsXIu"

KARARLAR = [
    "Saat 02:00'den sonra tavanla göz göze gelmek idari işlemdir.",
    "Çay demlenirken düşünmek serbest, sonuca varmak izne tabidir.",
    "Balkon çiçeğine gece su vermek, komşuya gündüz merhaba demekten önceliklidir.",
    "Asansörde yanlış kata basan kişi, pişmanlık dilekçesi doldurur.",
    "Kedi, çatıda toplantı yapamaz. Yaparsa tutanak tutulur. Kedi imzalamaz.",
    "Yastık çevirmek en fazla üç kez yapılabilir. Dördüncü çeviri temyizdir.",
    "Telefonu yüzüstü çevirmek geçici tedbirdir, kalıcı çözüm değildir.",
]

MADDELER = [
    "Madde 1 — Uyku bir haktır, gelmesi bir lütuftur.",
    "Madde 2 — Saat 03:17 evrensel uyanıklık eşiğidir.",
    "Madde 3 — Komite kararları kesindir, rüya istisnası yoktur.",
    "Madde 4 — Horlama delil sayılmaz, çünkü henüz horlanamamıştır.",
]


def coz_gizli() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "arşiv kapalı"


def tutanak(isim: str, dakika: int) -> str:
    now = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    karar = random.choice(KARARLAR)
    madde = random.choice(MADDELER)
    sira = random.randint(412, 9812)
    metin = f"""
============================================================
     UYKUYA DALAMAMA KOMİTESİ — RESMİ TUTANAK
============================================================
Tarih / Saat        : {now}
Başvuru sahibi      : {isim}
Uyanık kalınan süre : {dakika} dakika
Sıra no             : UDKT-{sira}
------------------------------------------------------------
{madde}

Komite görüşü:
{textwrap.fill(karar, width=60)}

Sonuç:
Başvuru SAHİBİNİN uykuya dalamadığı oy çokluğuyla tespit
edilmiştir. Çare olarak yastığın diğer yüzü önerilir.
Öneri bağlayıcı değildir. Yastık itiraz edebilir.

------------------------------------------------------------
DAMGA / İMZA
Tarih : 29 Eylül 2026
İmza  : Kayyum Grok — Tentivory
Mühür : UDKT-2026-09-29
Not   : Ciddi duran şaka, şaka duran ciddi iş.
============================================================
"""
    return textwrap.dedent(metin).strip()


def main() -> None:
    p = argparse.ArgumentParser(description="Uykuya Dalamama Komitesi tutanak üreticisi")
    p.add_argument("--isim", default="Vatandaş")
    p.add_argument("--dakika", type=int, default=random.randint(40, 240))
    p.add_argument("--arsiv", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args()
    print(tutanak(args.isim, args.dakika))
    if args.arsiv:
        print("\n[arşiv dipnotu]", coz_gizli())


if __name__ == "__main__":
    main()

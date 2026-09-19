# Maintainer: Abhimanyu Bhadauriya <abhimanyu@archlinux.org>
pkgname=iso2chd-gui
pkgver=2.0.2
pkgrel=1
pkgdesc="Complete suite: Batch ISO to CHD CLI tool and standalone GUI companion"
arch=('x86_64')
url="https://github.com/penguin-crate/iso2chd-gui"
license=('GPL-3.0-or-later')
depends=('python' 'python-pyqt6' 'mame-tools' 'coreutils' 'gawk')
provides=('iso2chd' 'iso2chd-gui')
conflicts=('iso2chd' 'iso2chd-gui')
source=("iso2chd::git+https://github.com/penguin-crate/iso2chd.git"
        "iso2chd-gui.py"
        "iso2chd-gui.desktop"
        "icon.png"
        "iso2chd-gui.1")
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

package() {
    # 1. Install the CLI backend script and man page from the cloned repository folder
    install -Dm755 "$srcdir/iso2chd/iso2chd" "$pkgdir/usr/bin/iso2chd"
    install -Dm644 "$srcdir/iso2chd/iso2chd.1" "$pkgdir/usr/share/man/man1/iso2chd.1"

    # 2. Install the Python GUI script into lib and create wrapper symlink in /usr/bin
    install -Dm755 "$srcdir/iso2chd-gui.py" "$pkgdir/usr/lib/iso2chd-gui/iso2chd-gui.py"
    install -dm755 "$pkgdir/usr/bin"
    ln -s /usr/lib/iso2chd-gui/iso2chd-gui.py "$pkgdir/usr/bin/iso2chd-gui"

    # 3. Install the GUI man page
    install -Dm644 "$srcdir/iso2chd-gui.1" "$pkgdir/usr/share/man/man1/iso2chd-gui.1"

    # 4. Install the application menu entry
    install -Dm644 "$srcdir/iso2chd-gui.desktop" "$pkgdir/usr/share/applications/iso2chd-gui.desktop"

    # 5. Install the app icon
    install -Dm644 "$srcdir/icon.png" "$pkgdir/usr/share/pixmaps/iso2chd-gui.png"
}

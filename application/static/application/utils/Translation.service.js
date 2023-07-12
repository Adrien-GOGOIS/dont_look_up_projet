class TranslationService {
	static isTranslate = false;
	static displayTranslation() {
		this.isTranslate = !this.isTranslate;
		if (this.isTranslate) {
			document.getElementById("translatedText").style.display = "block";
			document.getElementById("originalText").style.display = "none";
		} else {
			document.getElementById("translatedText").style.display = "none";
			document.getElementById("originalText").style.display = "block";
		}
	}
}

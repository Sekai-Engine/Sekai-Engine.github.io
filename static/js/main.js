document.addEventListener('DOMContentLoaded', () => {
	const downloadBtn = document.getElementById('downloadBtn');
	const downloadMenu = document.getElementById('downloadMenu');

	if (downloadBtn && downloadMenu) {
		downloadBtn.addEventListener('click', (e) => {
			e.preventDefault();
			downloadMenu.classList.toggle('show');
		});

		document.addEventListener('click', (e) => {
			if (!downloadBtn.contains(e.target) && !downloadMenu.contains(e.target)) {
				downloadMenu.classList.remove('show');
			}
		});
	}
});

// 阻止所有 # 链接实际跳转（保留UI）
document.querySelectorAll('a[href="#"]').forEach(a => {
	a.addEventListener('click', e => e.preventDefault());
});


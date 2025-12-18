// 主要JavaScript功能

// 获取模态框元素
const resultModal = document.getElementById('resultModal');
const imageModal = document.getElementById('imageModal');
const closeButtons = document.getElementsByClassName('close');

// 关闭模态框
Array.from(closeButtons).forEach(btn => {
    btn.onclick = function() {
        resultModal.style.display = 'none';
        imageModal.style.display = 'none';
    }
});

// 点击模态框外部关闭
window.onclick = function(event) {
    if (event.target == resultModal) {
        resultModal.style.display = 'none';
    }
    if (event.target == imageModal) {
        imageModal.style.display = 'none';
    }
}

// 运行策略
async function runStrategy(strategyId) {
    const resultContent = document.getElementById('resultContent');
    
    // 显示加载状态
    resultModal.style.display = 'block';
    resultContent.innerHTML = '<div class="loading">正在运行策略，请稍候</div>';
    
    try {
        const response = await fetch('/api/run_strategy', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                strategy_id: strategyId
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            resultContent.innerHTML = `
                <div style="color: red; padding: 20px;">
                    <h3>❌ 运行失败</h3>
                    <p>${data.error}</p>
                </div>
            `;
        } else {
            let output = '';
            
            if (data.stdout) {
                output += `
                    <div style="margin-bottom: 20px;">
                        <h3>✅ 运行成功</h3>
                        <h4>输出结果：</h4>
                        <pre>${escapeHtml(data.stdout)}</pre>
                    </div>
                `;
            }
            
            if (data.stderr) {
                output += `
                    <div style="margin-bottom: 20px;">
                        <h4>警告/错误信息：</h4>
                        <pre style="background: #fff3cd; color: #856404;">${escapeHtml(data.stderr)}</pre>
                    </div>
                `;
            }
            
            if (data.returncode === 0) {
                output += '<p style="color: green; font-weight: bold;">策略执行完成！</p>';
            } else {
                output += `<p style="color: red; font-weight: bold;">返回代码: ${data.returncode}</p>`;
            }
            
            resultContent.innerHTML = output;
        }
    } catch (error) {
        resultContent.innerHTML = `
            <div style="color: red; padding: 20px;">
                <h3>❌ 请求失败</h3>
                <p>${error.message}</p>
            </div>
        `;
    }
}

// 打开图片模态框
function openImageModal(imageSrc) {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');
    
    modal.style.display = 'block';
    modalImg.src = imageSrc;
}

// HTML转义函数
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// 页面加载完成后的初始化
document.addEventListener('DOMContentLoaded', function() {
    console.log('量化投资策略平台已加载');
    
    // 添加卡片动画
    const cards = document.querySelectorAll('.strategy-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 50);
    });
});

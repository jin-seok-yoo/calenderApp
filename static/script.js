var selFormArr = Array.from(Array(1), () => Array(2).fill(null))
var countSel = 0;
const day = document.querySelectorAll('td');
var daySel = $('.selected').length + 1
day.forEach((items)=>{
    items.addEventListener('click', (e)=>{
        
        // 선택한 날짜의 개수를 담는 변수
        daySel = $('.selected').length + 1

        // 선택한 날짜가 몇달인지 찾는 변수
        selMonth = $(items).parents('tr').parents('tbody').children('tr').first().text().trim()

        if(Number(items.innerHTML)){
            if(daySel > 1 && !items.classList.contains('selected')){
                // alert("Too Many Day")
                day.forEach((inItem)=>{
                    inItem.classList.remove('selected')
                });
                items.classList.toggle('selected');
                selFormArr[0][0] = selMonth;
                selFormArr[0][1] = items.innerHTML;
            }else{
                if(items.classList.contains('selected')){
                    // countSel --;                 
                }else{
                    selFormArr[0][0] = selMonth;
                    selFormArr[0][1] = items.innerHTML;
                    // countSel ++;
                }
                items.classList.toggle('selected');
            }
        }else{
            alert("Not a day");
        }
        e.stopPropagation();
        
    });
});


const sendBtn = document.querySelector('.sendBtn');
sendBtn.addEventListener('click', ()=>{
    $('#monthForm').val(selFormArr[0][0]);
    $('#dayForm').val(selFormArr[0][1]);
    // $('#dateSelForm').submit()
    console.log($('#monthForm').val());
    console.log($('#dayForm').val());
});
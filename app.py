@app.route('/result8', methods=['GET', 'POST'])
def result8():
    res = None
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        a_str = request.form.get('a', '').strip()
        b_str = request.form.get('b', '').strip()
        c_str = request.form.get('c', '').strip()

        try:
            a = int(a_str)
            b = int(b_str)
            c = int(c_str)
            sonlar_togri = True
        except ValueError:
            sonlar_togri = False

        if len(name) > 2 and sonlar_togri:
            yigindi = a + b + c
            orta_arifmetik = round((a + b + c) / 3, 2)
            maks = max(a, b, c)
            min_val = min(a, b, c)
            
            res = [name, a, b, c, yigindi, orta_arifmetik, maks, min_val]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result8.html', res=res)

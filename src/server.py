from datetime import datetime, timedelta
from flask import Flask, render_template
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
from database import Tablecoin, db,app
from selenium import webdriver
from bs4 import BeautifulSoup

db.engine.execute('drop table IF EXISTS NEWS')

db.engine.execute('CREATE TABLE NEWS (ID int, name_of_coin VARCHAR (255), news VARCHAR)')

db.session.commit()

app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

@app.route('/webpage')
def webpage():
    return render_template('form.html')


@app.route('/coin',  methods = ['POST', 'GET'])
def coin():
    if request.method == 'GET':
        return "GETTING DATA"

    if request.method == 'POST':
        names = request.form['name']
        url = 'https://coinmarketcap.com/currencies/'+ str(names) + "/news/"

        driver = webdriver.Firefox(executable_path=r'C:\Users\User\Downloads\geckodriver.exe')
        driver.get(url)
        page = driver.page_source
        soup = BeautifulSoup(page,'html.parser')

        filteredNews = []
        allNews = []
        allNews = soup.findAll('div', class_='sc-16r8icm-0 jKrmxw container')

        for i in range(len(allNews)):
            if allNews[i].find('p', class_='sc-1eb5slv-0 svowul-3 ddtKCV') is not None:
                filteredNews.append(allNews[i].text)

        for i, news_item in enumerate(filteredNews):
            print(i, f"{news_item}\n")


        for filteredParagraphs in filteredNews:
            new_ex = Tablecoin(1, names, filteredParagraphs)
            db.session.add(new_ex)
            db.session.commit()
           
            coins = db.engine.execute("select * from tablecoin where name_of_coin = '"+names+"'")
            return render_template("news.html", coins=coins)


if __name__ == '__main__':
    app.run(debug=True)
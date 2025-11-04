from pathlib import Path

from selene import browser, by, have, command


def test_fill_form():
    browser.open('/automation-practice-form')

    # Заполняю поля
    browser.element('#firstName').type('Daria')
    browser.element('#lastName').type('Tester')
    browser.element('#userEmail').type('daria.tester@example.com')
    browser.element(by.text('Female')).click()
    browser.element('#userNumber').type('9001234567')

    # Дата рождения — полностью через date-picker
    browser.element('#dateOfBirthInput').click() # открыть календарь
    browser.element('.react-datepicker__month-select').click().element(by.text('November')).click() # выбрать месяц
    browser.element('.react-datepicker__year-select').click().element(by.text('1995')).click() # выбрать год
    browser.element('.react-datepicker__day--003:not(.react-datepicker__day--outside-month)').click() # выбрать день,день 03 текущего месяца, не соседнего

    # Subjects — одно автодополнение + Enter
    browser.element('#subjectsInput').type('Math').press_enter()

    # Hobbies — выбираю Reading, чтобы прошла проверка ниже
    browser.element('#hobbiesWrapper').element(by.text('Reading')).click()

    # Загрузка картинки
    picture_path = str(Path(__file__).parent.parent.joinpath('resources', 'avatar.png').resolve())
    browser.element('#uploadPicture').set_value(picture_path)

    # Адрес
    browser.element('#currentAddress').type('Amsterdam, Keizersgracht 123')

    # State / City — это react-select
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    # Submit
    browser.element('#submit').click()

    # Минимально достаточная проверка появления модалки
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )

    # Таблица с результатами содержит наши значения
    browser.all('.modal-content table tbody tr td:nth-child(2)').should(have.exact_texts(
        'Daria Tester',
        'daria.tester@example.com',
        'Female',
        '9001234567',
        '03 November,1995',
        'Maths',
        'Reading',
        'avatar.png',
        'Amsterdam, Keizersgracht 123',
        'NCR Delhi'
    ))

// Файл со скриптом JavaScript для шаблонов приложения projects

// Функция для вывода сообщения в консоль браузера
function sayHello() {
  console.log("Hello from a static file!");
}

// Функция для добавления нового элемента списка на странице index.html
function addListItem() {
  // Получаем объект jQuery списка проектов
  var $list = $("#project-list");
  // Получаем объект jQuery поля ввода названия проекта
  var $input = $("#project-input");
  // Получаем значение поля ввода
  var title = $input.val();
  // Проверяем, что поле не пустое
  if (title) {
    // Создаем новый элемент списка с текстом из поля ввода
    var $item = $("<li></li>").text(title);
    // Добавляем новый элемент в конец списка
    $list.append($item);
    // Очищаем поле ввода
    $input.val("");
  }
}

// Функция для удаления последнего элемента списка на странице index.html
function removeListItem() {
  // Получаем объект jQuery списка проектов
  var $list = $("#project-list");
  // Удаляем последний дочерний элемент списка
  $list.children().last().remove();
}

// Функция для отправки данных формы на сервер с помощью AJAX на странице create.html
function submitForm() {
  // Получаем объект jQuery формы создания проекта
  var $form = $("#project-form");
  // Получаем URL-адрес, куда нужно отправить данные формы
  var url = $form.attr("action");
  // Получаем данные формы в виде объекта
  var data = $form.serialize();
  // Отправляем POST-запрос на сервер с данными формы
  $.post(url, data, function(response) {
    // Обрабатываем ответ сервера
    if (response.success) {
      // Если сервер вернул успех, то перенаправляем пользователя на страницу с деталями проекта
      window.location.href = response.detail_url;
    } else {
      // Если сервер вернул ошибку, то выводим сообщение об ошибке на странице
      $("#error-message").text(response.error_message);
    }
  });
}

// Функция для подтверждения удаления проекта на странице delete.html
function confirmDelete() {
  // Задаем текст вопроса для подтверждения удаления
  var question = "Вы действительно хотите удалить этот проект?";
  // Вызываем стандартное окно подтверждения браузера с текстом вопроса
  var answer = window.confirm(question);
  // Возвращаем ответ пользователя (true или false)
  return answer;
}

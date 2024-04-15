from model.driver_control import DriverControl

def js_click(driverControl:DriverControl,x_position:float, y_position:float):
    driverControl.driver.implicitly_wait(10)

    # Đoạn mã JavaScript để click vào vị trí x=100, y=100
    js_code = """
    var simulateClick = (x, y) => {
  var element = document.elementFromPoint(x, y); 

  var clickEvent = new MouseEvent('click', {
    'view': window,
    'bubbles': true,
    'cancelable': false
  });

  element.dispatchEvent(clickEvent); 

  var square = document.createElement('div');
  square.style.position = 'absolute';
  square.style.left = x + 'px';
  square.style.top = y + 'px';
  square.style.width = '10px';
  square.style.height = '10px';
  square.style.backgroundColor = 'red';
  document.body.appendChild(square);
};


    simulateClick("""+str(x_position)+""", """+str(y_position)+"""); 
    """

    # Thực thi đoạn mã JavaScript
    driverControl.driver.execute_script(js_code)



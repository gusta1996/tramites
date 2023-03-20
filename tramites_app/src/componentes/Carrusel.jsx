import Carousel from 'react-bootstrap/Carousel';
import 'bootstrap/dist/css/bootstrap.min.css';

export const Carrusel=() =>{
  return (
    <Carousel>
      <Carousel.Item style={{height: 'calc(90vh)'}}>
        <img
          className="d-block w-100"
          src="img1.jpg"
          alt="First slide"
          style={{height:'calc(90vh)'}}
        />
        <Carousel.Caption>
          <h3>First slide label</h3>
          <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item style={{height:'calc(90vh)'}}>
        <img
          className="d-block w-100"
          src="img2.jpg"
          alt="Second slide"
          style={{height:'calc(90vh)'}}
        />
        <Carousel.Caption>
          <h3>Second slide label</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item style={{height:'calc(90vh)'}}>
        <img
          className="d-block w-100"
          src="img1.jpg"
          alt="Third slide"
          style={{height:'calc(90vh)'}}
        />

        <Carousel.Caption>
          <h3>Third slide label</h3>
          <p>
            Praesent commodo cursus magna, vel scelerisque nisl consectetur.
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  );
}